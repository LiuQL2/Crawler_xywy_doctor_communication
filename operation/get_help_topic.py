# usr/bin/env python
# -*- coding: utf-8 -*-

from classes.mysqlDatabaseClass import MySQLDatabaseClass
from spiders.GetPostUrl import GetPostUrl
from spiders.HelpSpider import HelpSpider
from spiders.DoctorSpider import DoctorSpider
import datetime
import time
import csv



def get_help_topic(data_path, url_file, error_url_file, date_time,post_table_name, comment_first_table_name,
                   comment_second_table_name,doctor_table_name,doctor_url_split,afresh_post_url_file = True):

    while True:
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if date_time in crawl_time:
            break
        else:
            time.sleep(1)
            print 'waiting',crawl_time
            pass

    file_path = data_path
    help_topic_post_url_file = url_file
    help_topic_post_url_error_file = error_url_file
    start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if afresh_post_url_file == True:
        help_topic = GetPostUrl(file_path=file_path,case_experience_name=help_topic_post_url_file,help_topic_name=help_topic_post_url_file)
        help_topic.get_help_topic_post_url()
    else:
        pass

    file = open(file_path + help_topic_post_url_file,'r')
    reader = csv.reader(file)
    file_error = open(file_path + help_topic_post_url_error_file, 'wb')
    file_error.close()
    # file_error = open(file_path + help_topic_post_url_error_file, 'a+')
    # error_writer = csv.writer(file_error)
    error_number = 0
    mysql = MySQLDatabaseClass()
    for line in reader:
        print line[0],'********************************************************************************************************************************************'
        spider = HelpSpider(line[0])
        post_comment = spider.parse()
        if post_comment != False:
            post = post_comment['post']
            comment_list = post_comment['comment_list']
            mysql.insert(table=post_table_name,record=post)
            print '***帖子信息已入库'
            index = 1
            for comment in comment_list:
                mysql.insert(table=comment_first_table_name, record=comment['comment_first'])
                print '***第', str(index),'个一级评论已入库'
                index = index + 1
                for comment_second in comment['comment_second_list']:
                    parent_comment_list = (mysql.select(table=comment_first_table_name, record=comment['comment_first']))
                    if len(parent_comment_list) == 0:
                        print 'Error, not foud parent comment for:', comment_second
                        pass
                    else:
                        parent_comment = parent_comment_list[0]
                        comment_second['parent_comment_id'] = parent_comment['comment_id']
                        mysql.insert(table=comment_second_table_name, record=comment_second)
                        print '***二级评论已入库'
                        pass
            get_doctor_info(doctor_url_str=post['post_like_doctor_url'],split_str=doctor_url_split,table_name=doctor_table_name)
            get_doctor_info(doctor_url_str=post['post_comment_doctor_url'],split_str=doctor_url_split,table_name=doctor_table_name)
        else:
            print '#### Error!!'
            file_error = open(file_path + help_topic_post_url_error_file, 'a')
            error_writer = csv.writer(file_error)
            error_writer.writerow(line)
            file_error.close()
            error_number = error_number + 1
    file.close()
    mysql.close()
    # file_error.close()
    end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print 'number of error urls:', error_number
    print 'start time:', start_time
    print 'end time:', end_time


def get_doctor_info(doctor_url_str,split_str,table_name):
    mysql = MySQLDatabaseClass()
    doctor_url_list = doctor_url_str.split(split_str)
    for url in doctor_url_list:
        if 'club.xywy.com/doc_card' in url:
            doctor = DoctorSpider(url=url)
            doctor_info = doctor.get_number()
            if doctor_info != None:
                mysql.insert(table=table_name,record=doctor_info)
                print '医生信息已入库',url
            else:
                pass



if __name__ == '__main__':
    file_path = 'D:/Qianlong/PyCharmProjects/Crawler_xywy_doctor_communication/data/'
    help_topic_post_url_file = 'help_topic_url.csv'
    help_topic_post_url_error_file = 'help_topic_url_error.csv'
    date_time = '2016-12-10'
    post_table_name = 'help_topic_post'
    comment_first_table_name = 'help_topic_comment_first'
    comment_second_table_name = 'help_topic_comment_second'
    doctor_table_name = 'doctor'
    doctor_url_split = '#####'
    afresh_post_url_file = True
    get_help_topic(data_path=file_path,
                   url_file=help_topic_post_url_file,
                   error_url_file=help_topic_post_url_error_file,
                   date_time=date_time,
                   post_table_name=post_table_name,
                   comment_first_table_name=comment_first_table_name,
                   comment_second_table_name = comment_second_table_name,
                   doctor_table_name = doctor_table_name,
                   doctor_url_split = doctor_url_split,
                   afresh_post_url_file = afresh_post_url_file)
