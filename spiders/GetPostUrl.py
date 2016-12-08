#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
用来抓取病例和心得里面帖子URL的类，该类首先将帖子的URL保存在一个csv文件中。
对于URL保存的文件，在开始的时候如果存在的话，需要删除。
"""

# Author: Liu Qianlong  <LiuQL2@163.com>
# Date: 2016.11.06

import csv
import socket
import random
import sys
import urllib2
from urllib2 import URLError
import lxml.etree
from settings import USER_AGENTS as user_agents
import threading
reload(sys)
sys.setdefaultencoding('utf-8')


class MyException(Exception):
    pass


class GetPostUrl(object):
    def __init__(self,file_path, case_experience_name, help_topic_name,run_type = None, try_number = 20):
        """
        初始化一个实例，用来获取病例和心得下面的所有帖子的链接。
        :param post_url_path: 需要将帖子链接保存到的文件名及路径。
        """
        self.file_path = file_path
        self.case_experience_name =case_experience_name
        self.help_topic_name = help_topic_name
        self.run_type = run_type
        self.try_number = 20



        self.case_experience_start_urls = [
            'http://club.xywy.com/doctorShare/index/2',
            'http://club.xywy.com/doctorShare/index/3',
                        ]
        self.help_topic_start_urls = [
            'http://club.xywy.com/doctorShare/index/4',
            'http://club.xywy.com/doctorShare/index/5',
                        ]
        self.case_experience_page_urls = self.__get_page_url__(start_url_list=self.case_experience_start_urls)
        self.help_topic_page_urls = self.__get_page_url__(start_url_list=self.help_topic_start_urls)

    def run(self):
        if self.run_type == 'help_topic':
            self.get_help_topic_post_url()
        elif self.run_type == 'case_experience':
            self.get_case_experience_post_url()
        else:
            print 'please given the run type : "help_topic" or "case_experience"!'

    def __get_page_url__(self, start_url_list):
        page_url_list = []
        for start_url in start_url_list:
            request = urllib2.Request(url = start_url, headers= self.get_header())
            sel = None
            try_number = 0
            while sel == None:
                sel = self.process_request(request=request)
                try_number = try_number + 1
                if try_number > self.try_number:
                    break
                else:
                    pass
            if sel != None:
                page_number = int(sel.xpath('//div[@class="DocFen mt30 f14 cb"]/a[4]/text()')[0])
                print page_number, start_url
                stat = start_url.split('index/')[1]
                for index in range(1, page_number + 1, 1):
                    page_url_list.append(start_url + '?stat='+ stat + '&page=' + str(index))
            else:
                page_url_list = list()
        return page_url_list

    def get_case_experience_post_url(self):
        """
        获取每一页的帖子链接，并保存到文件。
        :return: 无返回内容
        """
        file = open(self.file_path + self.case_experience_name, 'wb')
        file_writer = csv.writer(file)
        page_url_list = self.case_experience_page_urls
        while len(page_url_list) != 0:
            error_case_experience_page_url_list = []
            for page_url in page_url_list:
                request = urllib2.Request(url=page_url, headers=self.get_header())
                sel = None
                try_number = 0
                while sel == None:
                    sel = self.process_request(request=request)
                    try_number = try_number + 1
                    if try_number > self.try_number:
                        break
                    else:
                        pass
                if sel != None:
                    post_url_list = sel.xpath('//div[@class="tab_Con pr"]/div[2]/div[1]/a/@href')
                    print len(post_url_list), page_url
                    for post_url in post_url_list:
                        file_writer.writerow([post_url,page_url])
                else:
                    error_case_experience_page_url_list.append(page_url)
            page_url_list = error_case_experience_page_url_list
        file.close()

    def get_help_topic_post_url(self):
        """
        获取每一页的帖子链接，并保存到文件。
        :return: 无返回内容
        """
        file = open(self.file_path + self.help_topic_name, 'wb')
        file_writer = csv.writer(file)
        page_url_list = self.help_topic_page_urls
        while len(page_url_list) != 0:
            error_help_topic_page_url_list = []
            for page_url in self.help_topic_page_urls:
                request = urllib2.Request(url=page_url, headers=self.get_header())
                sel = None
                try_number = 0
                while sel == None:
                    sel = self.process_request(request=request)
                    try_number = try_number + 1
                    if try_number > self.try_number:
                        break
                    else:
                        pass
                if sel != None:
                    post_url_list = sel.xpath('//div[@class="tab_Con pr"]/div[2]/div[1]/a/@href')
                    print len(post_url_list), page_url
                    for post_url in post_url_list:
                        file_writer.writerow([post_url, page_url])
                else:
                    error_help_topic_page_url_list.append(page_url)
            page_url_list = error_help_topic_page_url_list
        file.close()

    def get_header(self):
        """
        获得头文件。
        :return:返回一个header。
        """
        return {'User-Agent':random.choice(user_agents)}

    def process_request(self, request):
        """
        处理request请求
        :param request: 需要处理的request。
        :return:返回一个可以用xpath解析的selector格式。
        """
        try:
            response = urllib2.urlopen(request,timeout=100)
            try:
                doc = response.read()
                response.close()
                doc = doc.decode('GBK', 'ignore')
                doc = lxml.etree.HTML(doc)
            except:
                doc = None
                print 'return doc:None'
            return doc
        except URLError, e:
            if hasattr(e, 'reason'):
                print  'We failed to raach a server.'
                print  'Reaseon: ', e.reason
            elif hasattr(e, 'code'):
                print  'The server could not fulfill the request.'
                print  'Error code: ', e.code
                print  'Reason: ', e.reason
            return None
        except socket.timeout,e:
            # raise MyException('There was an error: %r' % e)
            print 'Error code: socket timeout', e
            return None
        except:
            print 'Do Not know what is wrong.'
            return None





if __name__ == '__main__':
    file_path = 'D:/Qianlong/PyCharmProjects/Crawler_xywy_doctor_communication/data/'
    case_experience_post_url_file = 'case_experience_url.csv'
    help_topic_post_url_file = 'help_topic_url.csv'
    spider = GetPostUrl(file_path=file_path,case_experience_name=case_experience_post_url_file,help_topic_name=help_topic_post_url_file)
    spider.get_case_experience_post_url()
    spider.get_help_topic_post_url()


