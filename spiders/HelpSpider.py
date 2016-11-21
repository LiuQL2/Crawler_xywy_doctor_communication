# usr/bin/env python
# -*- coding: utf-8 -*-

from CaseSpider import CaseSpider
import re
import sys
import datetime
import math
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')

class HelpSpider(CaseSpider):

    def __get_post_info__(self):
        post = {}
        post['post_url'] = self.target_url
        # post['post_title'] = self.selector.xpath('//h2[@class="pr fl  "]/text()')[0]
        mode = re.compile(r'\d+')
        post['post_review_number'] = mode.findall(self.selector.xpath('//div[@class="pulished_Left fl"]//span[@class="roat_tab fl"]/text()')[0])[0]
        post['post_time'] = self.selector.xpath('//div[@class="pulished_Left fl"]//span[@class="roat_tab fl"]/em/text()')[0]
        post_content = self.selector.xpath('////div[@class="duan_Luo pt10"]')
        post['post_content'] = post_content[0].xpath('string(.)')
        post['post_like_number'] = self.selector.xpath('//div[@class="function_Gn cb"]/div[3]/a[2]/span/text()')[0]
        post['post_like_doctor_url'] = self.__get_like_doctor_url__()

        if len(self.selector.xpath('//div[@class="tab_Ralax clearfix"]/span/a/@href')) == 0:
            post['post_doctor_url'] = '匿名用户'
        else:
            post['post_doctor_url'] = self.selector.xpath('//div[@class="tab_Ralax clearfix"]/span/a/@href')[0]
        post['post_follower_number'] = self.selector.xpath('//div[@class="for_Health"]/h2/span/text()')[0]
        post['post_type'] = self.selector.xpath('//div[@class="pulished2 w1000 bc clearfix f12 fgray"]/a[2]/text()')[0]
        post['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #以下获取评论的部分信息
        comment = self.__get_comment_doctor__()
        post['post_comment_doctor_url'] = comment['comment_doctor_url']
        post['post_comment_number'] = comment['comment_number']
        print post['post_url']
        # print post['post_title']
        print post['post_review_number']
        print post['post_time']
        print post['post_content']
        print post['post_like_number']
        print post['post_like_doctor_url']
        print post['post_comment_number']
        print post['post_comment_doctor_url']
        print post['post_doctor_url']
        print post['post_follower_number']
        print post['post_type']
        print post['crawl_time']
        return post

    def __get_comment_page_url__(self):
        """
        用来获取评论内容的详情页和评论的数量。
        :return: 返回一个字典，评论的详情页和评论的数量。
        """
        id = self.target_url.split('detail/')[1]
        comment_number = self.selector.xpath('//div[@class="function_Gn cb"]/div[3]/a[1]/span/text()')[0]
        if comment_number == '评论':
            comment_number = 0
            # print comment_number
        elif comment_number == '回答':
            comment_number = 0
        else:
            comment_number = int(self.selector.xpath('//div[@class="function_Gn cb"]/div[3]/a[1]/span/text()')[0])
        page_number = int(math.ceil(float(comment_number) / 10))
        comment_url = 'http://club.xywy.com/doctorShare/index.php?type=share_operation&page='+ str(page_number) + '&stat=15&share_id='+ str(id)
        return {'comment_page_url':comment_url, 'comment_number':comment_number}


# help = HelpSpider('http://club.xywy.com/doctorShare/detail/52848')
# help = HelpSpider('http://club.xywy.com/doctorShare/detail/52771')
# help.__get_post_info__()
# print help.__get_comment__()

