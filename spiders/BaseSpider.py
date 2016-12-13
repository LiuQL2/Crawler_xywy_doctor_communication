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
    # def __init__(self):
    #     pass

    def get_header(self):
        """
        获得头文件。
        :return:返回一个header。
        """
        return {'User-Agent':random.choice(user_agents)}

    def process_url_request(self,url,try_number=20, timeout=100,xpath_type=True, wether_decode=False, encode_type='utf-8'):
        doc = None
        try_index = 0
        if xpath_type == True:
            while doc == None:
                request = urllib2.Request(url=url, headers=self.get_header())
                doc = self.__process_request_xpath__(request=request,timeout=timeout,wether_decode=wether_decode, encode_type=encode_type)
                try_index = try_index + 1
                if try_index > try_number:
                    break
                else:
                    pass
            return doc
        else:
            while doc == None:
                request = urllib2.Request(url=url, headers=self.get_header())
                doc = self.__process_request__(request=request,timeout=timeout)
                try_index = try_index + 1
                if try_index > try_number:
                    break
                else:
                    pass
            return doc

    def __process_request_xpath__(self,request,timeout=100, wether_decode=False,encode_type='utf-8'):
        """
        处理request请求
        :param request: 需要处理的request。
        :return:返回一个可以用xpath解析的selector格式。
        """
        try:
            response = urllib2.urlopen(request,timeout=timeout)
            try:
                doc = response.read()
                response.close()
                if wether_decode == True:
                    doc = doc.decode(encode_type, 'ignore')
                else:
                    pass
                doc = lxml.etree.HTML(doc)
            except:
                doc = None
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

    def __process_request__(self,request,timeout = 100):
        try:
            response = urllib2.urlopen(request, timeout=timeout)
            doc = response.read()
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