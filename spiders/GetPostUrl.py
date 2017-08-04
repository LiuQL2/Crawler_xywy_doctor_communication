#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
用来抓取病例和心得里面帖子URL的类，该类首先将帖子的URL保存在一个csv文件中。
对于URL保存的文件，在开始的时候如果存在的话，需要删除。
"""

# Author: Liu Qianlong  <LiuQL2@163.com>
# Date: 2016.11.06

import sys
import json
import threading

from BaseSpider import BaseSpider
from database.RabbitMQ import RabbitmqServer
from configuration.settings import USE_PROXY as use_proxy
from configuration.settings import POST_URL_QUEUE_EXCHANGE as post_url_queue_exchange

reload(sys)
sys.setdefaultencoding('utf-8')


class GetPostUrl(BaseSpider):
    def __init__(self, try_number = 20):
        """
        初始化一个实例，用来获取病例和心得下面的所有帖子的链接。
        :param post_url_path: 需要将帖子链接保存到的文件名及路径。
        """
        self.try_number = 20
        self.timeout = 100

        self.case_experience_start_urls = [
            'http://club.xywy.com/doctorShare/index/2',
            'http://club.xywy.com/doctorShare/index/3',
                        ]
        self.help_topic_start_urls = [
            'http://club.xywy.com/doctorShare/index/4',
            'http://club.xywy.com/doctorShare/index/5',
                        ]

    def __get_page_url__(self, start_url_list):
        page_url_list = []
        for start_url in start_url_list:
            sel = self.process_url_request(url=start_url,timeout=self.timeout,try_number=self.try_number,xpath_type=True,whether_decode=True,encode_type='GBK',use_proxy=use_proxy)
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
        page_url_list =  self.__get_page_url__(start_url_list=self.case_experience_start_urls)
        while len(page_url_list) != 0:
            error_case_experience_page_url_list = []
            for page_url in page_url_list:
                sel = self.process_url_request(url = page_url,try_number=self.try_number,timeout=self.timeout,xpath_type=True,whether_decode=True,encode_type='GBK',use_proxy=use_proxy)
                if sel != None:
                    post_url_list = sel.xpath('//div[@class="tab_Con pr"]/div[2]/div[1]/a/@href')
                    print len(post_url_list), page_url
                    for post_url in post_url_list:
                        message={}
                        message['type'] = 'case_experience'
                        message['content'] = post_url
                        RabbitmqServer.add_message(message=json.dumps(message),
                                                   routing_key=post_url_queue_exchange['routing_key'],
                                                   queue=post_url_queue_exchange['queue'],
                                                   queue_durable=post_url_queue_exchange['queue_durable'],
                                                   exchange=post_url_queue_exchange['exchange'],
                                                   exchange_type=post_url_queue_exchange['exchange_type']
                                                   )
                else:
                    error_case_experience_page_url_list.append(page_url)
            page_url_list = error_case_experience_page_url_list

    def get_help_topic_post_url(self):
        """
        获取每一页的帖子链接，并保存到文件。
        :return: 无返回内容
        """
        page_url_list = self.__get_page_url__(start_url_list=self.help_topic_start_urls)
        while len(page_url_list) != 0:
            error_help_topic_page_url_list = []
            for page_url in page_url_list:
                sel = self.process_url_request(url=page_url, try_number=self.try_number, timeout=self.timeout,
                                               xpath_type=True, whether_decode=True, encode_type='GBK',use_proxy=use_proxy)
                if sel != None:
                    post_url_list = sel.xpath('//div[@class="tab_Con pr"]/div[2]/div[1]/a/@href')
                    print len(post_url_list), page_url
                    for post_url in post_url_list:
                        message={}
                        message['type'] = 'help_topic'
                        message['content'] = post_url
                        RabbitmqServer.add_message(message=json.dumps(message),
                                                   routing_key=post_url_queue_exchange['routing_key'],
                                                   queue=post_url_queue_exchange['queue'],
                                                   queue_durable=post_url_queue_exchange['queue_durable'],
                                                   exchange=post_url_queue_exchange['exchange'],
                                                   exchange_type=post_url_queue_exchange['exchange_type']
                                                   )
                else:
                    error_help_topic_page_url_list.append(page_url)
            page_url_list = error_help_topic_page_url_list

    def get_post_url(self):
        """
        多线程，同时获取case_experience和help_topic的帖子url。
        :return:
        """
        threads = []
        task1 = threading.Thread(target=self.get_case_experience_post_url)
        task2 = threading.Thread(target=self.get_help_topic_post_url)
        threads.append(task1)
        threads.append(task2)
        for task in threads:
            task.setDaemon(True)
            task.start()
        for task in threads:
            task.join()





if __name__ == '__main__':
    spider = GetPostUrl()
    spider.get_post_url()


