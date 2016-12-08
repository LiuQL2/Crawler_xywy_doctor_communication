#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
用来获取病例和心得帖子内容的类，传入一个帖子的URL，调用不同的方法得到不同的数据。
"""

# Author: Liu Qianlong <LiuQL2@163.com>
# Date: 2016.12.08

import datetime
import math
import random
import re
import socket
import json
import sys
import urllib2
from urllib2 import URLError
from BaseSpider import BaseSpider

import lxml.etree

from settings import USER_AGENTS as user_agents

reload(sys)
sys.setdefaultencoding('utf-8')

class DoctorSpider(BaseSpider):
    def __init__(self,url, try_number = 20):
        self.target_url = url
        request = urllib2.Request(url=self.target_url, headers=self.get_header())
        self.status = True
        self.try_number = try_number
        self.selector = None
        self.number_url = 'http://club.xywy.com/doctorShare/index.php?type=share_operation&uid=' + self.target_url.split('/')[4] + '&stat=14'
        # index = 0
        # while self.selector == None:
        #     index = index + 1
        #     self.selector = self.process_request(request=request)
        #     if index > self.try_number:
        #         self.status = False
        #         break

    def get_number(self):
        request = urllib2.Request(url=self.number_url, headers=self.get_header())
        doc = None
        try_index = 0
        while doc == None:
            doc = self.process_request_json(request=request)
            if try_index > self.try_number:
                self.status = False
                break
            else:
                pass
        if doc != None:
            doc = json.loads(doc)
            crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')
            print doc['fansNum']
            print doc['attenNum']
            print doc['wbNum']
            return {'attention_number':str(doc['attenNum']), 'fans_number':str(doc['fansNum']),'web_number':str(doc['wbNum']),'doctor_url':self.target_url, 'crawl_time':crawl_time}
        else:
            return None


if __name__ == '__main__':
    doctor = DoctorSpider(url='http://club.xywy.com/doc_card/55316663/blog')
    print doctor.get_number()