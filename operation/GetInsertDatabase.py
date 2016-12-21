# usr/bin/env python
# -*- coding: utf-8 -*-

from classes.MysqlDatabaseClass import MySQLDatabaseClass
from spiders.GetPostUrl import GetPostUrl
from spiders.HelpSpider import HelpSpider
from spiders.DoctorSpider import DoctorSpider
import datetime
import time
import csv



class GetData(object):
    def __init__(self,crawl_number, data_path, url_file, error_url_file, success_url_file,date_time,post_table_name, comment_first_table_name,
                   comment_second_table_name,doctor_table_name,doctor_url_only_table_name,post_type,doctor_url_split,afresh_post_url_file = True):
        self.crawl_number = crawl_number
        self.data_path = data_path
        self.url_file = url_file
        self.error_url_file = error_url_file
        self.success_url_file = success_url_file
        self.date_time = date_time
        self.post_table_name = post_table_name
        self.comment_first_table_name = comment_first_table_name
        self.comment_second_table_name = comment_second_table_name
        self.doctor_table_name = doctor_table_name
        self.doctor_url_split = doctor_url_split
        self.post_type = post_type
        self.afresh_post_url_file = afresh_post_url_file
        self.doctor_url_only_table_name = doctor_url_only_table_name
        self.mysql = MySQLDatabaseClass()

    def get_data(self):
        while True:
            crawl_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if self.date_time in crawl_time:
                break
            else:
                time.sleep(1)
                print 'waiting', crawl_time
                pass

        start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if self.afresh_post_url_file == True:
            get_post = GetPostUrl(file_path=self.data_path, case_experience_name=self.url_file, help_topic_name=self.url_file)
            get_post.get_help_topic_post_url()
        else:
            pass

        file = open(self.data_path + self.url_file, 'r')
        reader = csv.reader(file)
        file_error = open(self.data_path + self.error_url_file, 'wb')
        file_error.close()

        success_file = open(self.data_path + self.success_url_file, 'wb')
        success_writer = csv.writer(success_file)

        error_number = 0
        if self.post_type == 'help_topic':
            from spiders.HelpSpider import HelpSpider as PostSpider
        else:
            from spiders.CaseSpider import CaseSpider as PostSpider
        for line in reader:
            if len(line) != 0:
                print line[
                    0], '********************************************************************************************************************************************'
                spider = PostSpider(line[0], crawl_number=self.crawl_number)
                post_comment = spider.parse()
            else:
                post_comment = False

            if post_comment != False:
                post = post_comment['post']
                comment_list = post_comment['comment_list']
                self.mysql.insert(table=self.post_table_name, record=post)
                print '***帖子信息已入库'
                index = 1
                for comment in comment_list:
                    self.mysql.insert(table=self.comment_first_table_name, record=comment['comment_first'])
                    print '***第', str(index), '个一级评论已入库'
                    index = index + 1
                    for comment_second in comment['comment_second_list']:
                        parent_comment_list = (
                            self.mysql.select(table=self.comment_first_table_name, record=comment['comment_first']))
                        if len(parent_comment_list) == 0:
                            print 'Error, not foud parent comment for:', comment_second
                            pass
                        else:
                            parent_comment = parent_comment_list[0]
                            # comment_second['parent_comment_id'] = parent_comment['comment_id']
                            comment_second['parent_comment_doctor_url'] = parent_comment['doctor_url']
                            comment_second['parent_comment_comment_time'] = parent_comment['comment_time']
                            comment_second['parent_comment_comment_content'] = parent_comment['comment_content']
                            self.mysql.insert(table=self.comment_second_table_name, record=comment_second)
                            print '***二级评论已入库'
                            pass
                self.insert_doctor_url(doctor_url_list=post['post_like_doctor_url'],  split=True)
                self.insert_doctor_url(doctor_url_list=post['post_comment_doctor_url'],split=True)
                self.insert_doctor_url(doctor_url_list=[post['post_doctor_url']])
                success_writer.writerow(line)
            else:
                print '#### Error!!'
                file_error = open(self.data_path + self.error_url_file, 'a')
                error_writer = csv.writer(file_error)
                error_writer.writerow(line)
                file_error.close()
                error_number = error_number + 1
        file.close()
        success_file.close()
        end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print 'number of error urls:', error_number
        print 'start time:', start_time
        print 'end time:', end_time

    def get_doctor_info(self,doctor_url_str):
        mysql = MySQLDatabaseClass()
        doctor_url_list = doctor_url_str.split(self.doctor_url_split)
        for url in doctor_url_list:
            if 'club.xywy.com/doc_card' in url:
                doctor = DoctorSpider(url=url, crawl_number=self.crawl_number)
                doctor_info = doctor.get_number()
                if doctor_info != None:
                    mysql.insert(table=self.doctor_table_name, record=doctor_info)
                    print '医生信息已入库', url
                else:
                    pass

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
                self.mysql.insert(table=self.doctor_table_name, record=doctor_info)
                doctor_info['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d')
                self.mysql.insert(table=self.doctor_url_only_table_name, record=doctor_info)

    def update_doctor_info(self):
        doctor_dict_list = self.mysql.select(table=self.doctor_table_name, record={'crawl_number': self.crawl_number})
        for doctor_dict in doctor_dict_list:
            url = doctor_dict['doctor_url']
            doctor = DoctorSpider(url=url, crawl_number=self.crawl_number)
            doctor_info = doctor.get_number()
            if doctor_info != None:
                self.mysql.update(table=self.doctor_table_name, record=doctor_info,
                             primary_key={'doctor_url': url, 'crawl_number': doctor_dict['crawl_number']})
                print '医生信息已入库', url
            else:
                pass

    def close_database(self):
        self.mysql.close()