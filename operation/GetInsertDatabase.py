# usr/bin/env python
# -*- coding: utf-8 -*-

import json
from database.MysqlDatabaseClass import MySQLDatabaseClass
from spiders.DoctorSpider import DoctorSpider
from configuration.settings import TABLE_INFO as table_info
from configuration.settings import CRAWL_NUMBER as crawl_number
import datetime


class InsertDatabase(object):
    def __init__(self, message, doctor_url_split, crawl_number):
        self.type = message['type']
        self.post_comment = json.loads(message['content'])
        self.mysql = MySQLDatabaseClass()
        self.doctor_url_split = doctor_url_split
        self.crawl_number = crawl_number

    def process(self):
        post = self.post_comment['post']
        comment_list = self.post_comment['comment_list']
        self.mysql.insert(table=table_info[self.type]['post'], record=post)
        print '***帖子信息已入库'
        index = 1
        for comment in comment_list:
            self.mysql.insert(table=table_info[self.type]['comment_first'], record=comment['comment_first'])
            print '***第', str(index), '个一级评论已入库'
            index = index + 1
            for comment_second in comment['comment_second_list']:
                parent_comment_list = self.mysql.select(table=table_info[self.type]['comment_first'], record=comment['comment_first'])
                if len(parent_comment_list) == 0:
                    print 'Error, not find parent comment for:', comment_second
                    pass
                else:
                    parent_comment = parent_comment_list[0]
                    comment_second['parent_comment_doctor_url'] = parent_comment['doctor_url']
                    comment_second['parent_comment_comment_time'] = parent_comment['comment_time']
                    comment_second['parent_comment_comment_content'] = parent_comment['comment_content']
                    self.mysql.insert(table=table_info[self.type]['comment_second'], record=comment_second)
                    print '***二级评论已入库'
                    pass
        self.insert_doctor_url(doctor_url_list=post['post_like_doctor_url'],  split=True)
        self.insert_doctor_url(doctor_url_list=post['post_comment_doctor_url'],split=True)
        self.insert_doctor_url(doctor_url_list=[post['post_doctor_url']])

    def insert_doctor_url(self,doctor_url_list, split=False):
        if split == True:
            doctor_url_list = doctor_url_list.split(self.doctor_url_split)
        else:
            pass
        for url in doctor_url_list:
            if 'club.xywy.com/doc_card' in url:
                doctor_info = {}
                doctor_info['doctor_url'] = url
                doctor_info['crawl_number'] = self.crawl_number
                print doctor_info
                self.mysql.insert(table=table_info['doctor_communication'], record=doctor_info)
                doctor_info['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d')
                self.mysql.insert(table=table_info['doctor_url'], record=doctor_info)

    @staticmethod
    def update_doctor_info():
        """
        跟新这次抓取的医生信息
        :return:
        """
        mysql = MySQLDatabaseClass()
        doctor_dict_list = mysql.select(table=table_info['doctor_communication'], record={'crawl_number': crawl_number})
        for doctor_dict in doctor_dict_list:
            url = doctor_dict['doctor_url']
            doctor = DoctorSpider(url=url, crawl_number=crawl_number)
            doctor_info = doctor.get_number()
            if doctor_info != None:
                mysql.update(table=table_info['doctor_communication'], record=doctor_info,
                             primary_key={'doctor_url': url, 'crawl_number': doctor_dict['crawl_number']})
                print '医生信息已入库', url
            else:
                pass
        mysql.close()

    def close(self):
        self.mysql.close()