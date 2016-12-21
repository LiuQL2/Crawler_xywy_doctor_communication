#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
用来获取病例和心得帖子内容的类，传入一个帖子的URL，调用不同的方法得到不同的数据。
"""

# Author: Liu Qianlong <LiuQL2@163.com>
# Date: 2016.11.06

import datetime
import math
import random
import re
import sys
import urllib2
from urllib2 import URLError
from BaseSpider import BaseSpider

reload(sys)
sys.setdefaultencoding('utf-8')


class CaseSpider(BaseSpider):
    def __init__(self, url, crawl_number, try_number=20, timeout=100):
        """
        实例的初始化，传入一个URL之后完成request，并构建selector
        :param url:需要抓取的一个帖子的链接
        """
        self.target_url = url
        self.status = True
        self.try_number = try_number
        self.crawl_number = crawl_number
        self.timeout = timeout
        self.selector = self.process_url_request(url=self.target_url, try_number=self.try_number, xpath_type=True,whether_decode=True,encode_type='GBK')
        if self.selector == None:
            self.status = False
        else:
            pass

    def parse(self):
        """
        用来抓取帖子信息的方法，分为两部分：帖子的信息post，和评论信息：comment。其中评论信息分为一级和二级评论，两部分都是通过调用函数完成
        :return:以字典的形式返回数据。其中post是字典，comment_list是一个包含多个字典的list。
        """
        if self.status == True:
            post = self.__get_post_info__()
        else:
            post = None
        print post
        if self.status == True:
            comment_list = self.__get_comment__()
        else:
            comment_list = None
        if self.status == True:
            return {'post':post, 'comment_list':comment_list}
        else:
            return False

    def __get_post_info__(self):
        """
        用来获取post信息的帖子，包含各种信息
        :return: 以字典的形式返回该post的主要信息。
        """
        try:
            post = {}
            post['crawl_number'] = self.crawl_number
            post['post_url'] = self.target_url
            post['post_title'] = self.selector.xpath('//h2[@class="pr fl w540 "]/text()')[0]
            mode = re.compile(r'\d+')
            post['post_review_number'] = mode.findall(self.selector.xpath('//div[@class="pulished_Left fl"]//span[@class="roat_tab fl"]/text()')[0])[0]
            post['post_time'] = self.selector.xpath('//div[@class="pulished_Left fl"]//span[@class="roat_tab fl"]/em/text()')[0]
            post_content = self.selector.xpath('//div[@class="duan_Luo pt10"]')
            post['post_content'] = post_content[0].xpath('string(.)')
            post['post_like_number'] = self.selector.xpath('//div[@class="function_Gn cb"]/div[2]/a[2]/span/text()')[0]
            post['post_like_doctor_url'] = self.__get_like_doctor_url__()

            #以下获取评论的部分信息
            comment = self.__get_comment_doctor__()
            if comment != None:
                post['post_comment_doctor_url'] = comment['comment_doctor_url']
                post['post_comment_number'] = comment['comment_number']
                post_doctor_url = self.selector.xpath('//div[@class="doc_Toux clearfix"]/div[@class="fl ml15"]/a/@href')
                #以下获取发帖人的信息，因为有些不是医生发帖，所以这里就要分情况讨论。
                if len(post_doctor_url) == 0:
                    post['post_doctor_url'] = (self.selector.xpath('//div[@class="doc_Toux clearfix"]/div[@class="fl ml15"]/text()[1]')[0].replace(' ', '')).replace('/blog', '')
                else:
                    post['post_doctor_url'] = (self.selector.xpath('//div[@class="doc_Toux clearfix"]/div[@class="fl ml15"]/a/@href')[0]).replace('/blog', '')
                dynamic_fans = self.selector.xpath('//div[@class="doc_Toux clearfix"]/div[@class="fl ml15"]/p/span/em/text()')
                post['post_doctor_dynamic'] = dynamic_fans[0]
                post['post_doctor_fans'] = dynamic_fans[1]
                post['post_type'] = self.selector.xpath('//div[@class="pulished2 w1000 bc clearfix f12 fgray"]/a[2]/text()')[0]
                # post['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                post['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d')

                return post
            else:
                return None
        except:
            self.status = False
            return None


    def __get_like_doctor_url__(self):
        """
        获取该话题下点赞医生的链接，当点赞人数较多时，不能全部显示，也不能全部获取。
        :param selector: 话题网页源码转化为可以用Xpath的格式后数据
        :return:返回一个字符串，用分割符分割的点赞医生链接。
        """
        if self.selector != None:
            try:
                doctor_url_list = self.selector.xpath('//div[@class="fl approve_con approve_con_short"]/span/a/@href')
                temp = ''
                separator = '#####'
                for url in doctor_url_list:
                    temp = temp + url.replace('/blog', '') + separator
                return temp[0:len(temp)]
            except:
                self.status = False
                return None
        else:
            return None

    def __get_comment_doctor__(self):
        """
        用来获取评论医生的链接和评论医生的数量，同时将医生互相评论的部分也作为一级评论返回。
        :return:返回一个字典，包含评论数和评论医生的链接。
        """
        comment_page_number = self.__get_comment_page_url__()
        comment_url = comment_page_number['comment_page_url']
        comment_selector = self.process_url_request(url=comment_url,try_number=self.try_number,xpath_type=True,encode_type='GBK')

        if comment_selector != None:
            doctor_url_list = comment_selector.xpath('//div[@class="dis_List clearfix pr"]/div[2]/div[1]/a/@href')
            comment_doctor_url = ''
            separator = '#####'
            for url in doctor_url_list:
                if url.replace('/blog', '') not in comment_doctor_url:
                    comment_doctor_url = comment_doctor_url + url.replace('/blog', '') + separator
                else:
                    pass

            reply_doctor_url_list = comment_selector.xpath('//div[@class="dis_List clearfix pr"]//div[@class="dis_List clearfix"]/div[2]/div[1]/a[1]/@href')
            # print len(reply_doctor_url_list)
            if len(reply_doctor_url_list) != 0:
                comment_doctor_url = comment_doctor_url + separator
            for url in reply_doctor_url_list:
                if url.replace('/blog', '') not in comment_doctor_url:
                    comment_doctor_url = comment_doctor_url + url.replace('/blog', '') + separator
                else:
                    pass
            return {'comment_doctor_url':comment_doctor_url, 'comment_number':comment_page_number['comment_number']}
        else:
            self.status = False
            return None

    def __get_comment__(self):
        """
        用来获取评论的详细内容的方法，包括评论医生链接、内容等，还有针对某一条评论医生之间的互相回复。
        :return: 返回一个list，其中每一个元素是一个一级评论，一级评论里面可能有二级评论的内容。
        """
        comment_url = self.__get_comment_page_url__()['comment_page_url']
        comment_selector = self.process_url_request(url=comment_url, try_number=self.try_number,whether_decode=True, xpath_type=True,encode_type='GBK')

        if comment_selector != None:
            comment_content_list = comment_selector.xpath('//div[@class="dis_List clearfix pr"]')
            # crawl_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')
            comment_list = []

            for comment_temp in comment_content_list:
                comment = {}
                comment_first = {}
                comment_first['post_url'] = self.target_url
                comment_first['crawl_number'] = self.crawl_number
                if len(comment_temp.xpath('div[2]/div[1]/a/@href')) == 0:
                    comment_first['doctor_url'] = '匿名用户'
                else:
                    comment_first['doctor_url'] = (comment_temp.xpath('div[2]/div[1]/a/@href')[0]).replace('/blog','')
                comment_first['comment_time'] = comment_temp.xpath('div[2]/div[1]/span/text()')[0]

                # comment_first['comment_content'] = comment_temp.xpath('div[2]/p[@class="mt10"]/text()')[0]
                temp = comment_temp.xpath('div[2]/p[@class="mt10"]')
                if len(temp[0].xpath('string(.)')) != 0:
                    comment_first['comment_content'] = temp[0].xpath('string(.)')
                else:
                    comment_first['comment_content'] = ''
                comment_first['crawl_time'] = crawl_time

                #以下为获得二级评论内容。
                comment_second_content = comment_temp.xpath('div[2]//div[@class="dis_List clearfix"]')
                index = 1
                comment_second_list = []
                for comment_second_temp in comment_second_content:
                    comment_second  ={}
                    comment_second['post_url'] = self.target_url
                    comment_second['crawl_number'] = self.crawl_number
                    if len(comment_second_temp.xpath('div[2]/div[1]/a/@href')) == 2:
                        comment_second['reply_to_doctor'] = (comment_second_temp.xpath('div[2]/div[1]/a/@href')[1]).replace('/blog','')
                        comment_second['reply_doctor'] = (comment_second_temp.xpath('div[2]/div[1]/a/@href')[0]).replace('/blog','')
                    elif len(comment_second_temp.xpath('div[2]/div[1]/a/@href')) == 1:
                        comment_second['reply_to_doctor'] = '匿名用户'
                        comment_second['reply_doctor'] = (comment_second_temp.xpath('div[2]/div[1]/a/@href')[0]).replace('/blog','')
                    elif len(comment_second_temp.xpath('div[2]/div[1]/a/@href')) == 0:
                        comment_second['reply_to_doctor'] = '匿名用户'
                        comment_second['reply_doctor'] = '匿名用户'
                    comment_second['reply_time'] = comment_second_temp.xpath('div[2]/div[1]/span[2]/text()')[0]

                    # comment_second['reply_content'] = comment_second_temp.xpath('div[2]/p/text()')[0]
                    reply_content_temp = comment_second_temp.xpath('div[2]/p')
                    comment_second['reply_content'] = reply_content_temp[0].xpath('string(.)')
                    print comment_second['reply_content']
                    comment_second['sequence'] = index
                    comment_second['crawl_time'] = crawl_time
                    index = index + 1
                    comment_second_list.append(comment_second)
                comment['comment_first'] = comment_first
                comment['comment_second_list'] = comment_second_list
                comment_list.append(comment)

            return comment_list
        else:
            self.status = False
            return None

    def __get_comment_page_url__(self):
        """
        用来获取评论内容的详情页和评论的数量。
        :return: 返回一个字典，评论的详情页和评论的数量。
        """
        if self.selector != None:
            id = self.target_url.split('detail/')[1]
            comment_number = self.selector.xpath('//div[@class="function_Gn cb"]/div[2]/a[1]/span/text()')[0]
            if comment_number == '评论':
                comment_number = 0
            else:
                comment_number = int(self.selector.xpath('//div[@class="function_Gn cb"]/div[2]/a[1]/span/text()')[0])
            page_number = int(math.ceil(float(comment_number) / 10))
            comment_url = 'http://club.xywy.com/doctorShare/index.php?type=share_operation&page='+ str(page_number) + '&stat=15&share_id='+ str(id)
            return {'comment_page_url':comment_url, 'comment_number':comment_number}
        else:
            return None



if __name__ == '__main__':
    # spider = CaseSpider('http://club.xywy.com/doctorShare/detail/8332')
    # spider = CaseSpider('http://club.xywy.com/doctorShare/detail/22315')
    # spider = CaseSpider('http://club.xywy.com/doctorShare/detail/52406')
    # spider = CaseSpider('http://club.xywy.com/doctorShare/detail/51393')
    spider = CaseSpider('http://club.xywy.com/doctorShare/detail/53166')
    print spider.parse()
