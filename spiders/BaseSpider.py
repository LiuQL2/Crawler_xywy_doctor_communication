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


class BaseSpider(object):
    def __init__(self):
        pass

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

    def process_request_json(self,request):
        try:
            response = urllib2.urlopen(request, timeout=100)
            doc = response.read()
            return doc
        except:
            print 'Error: get json from server.'
            return None