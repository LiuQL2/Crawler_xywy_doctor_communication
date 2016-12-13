# usr/bin/env python
# -*- coding: utf-8 -*-

from classes.mysqlDatabaseClass import MySQLDatabaseClass
from spiders.GetPostUrl import GetPostUrl
from spiders.HelpSpider import HelpSpider
from spiders.DoctorSpider import DoctorSpider
import datetime
import time
import csv



def get_data(crawl_number, data_path, url_file, error_url_file, date_time,post_table_name, comment_first_table_name,
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
    start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if afresh_post_url_file == True:
        get_post = GetPostUrl(file_path=file_path,case_experience_name=url_file,help_topic_name=url_file)
        get_post.get_help_topic_post_url()
    else:
        pass

    file = open(file_path + url_file,'r')
    reader = csv.reader(file)
    file_error = open(file_path + error_url_file, 'wb')
    file_error.close()
    error_number = 0
    mysql = MySQLDatabaseClass()
    for line in reader:
        if len(line) != 0:
            print line[0],'********************************************************************************************************************************************'
            spider = HelpSpider(line[0],crawl_number=crawl_number)
            post_comment = spider.parse()
        else:
            post_comment = False

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
                    # parent_comment_list = (mysql.select(table=comment_first_table_name, record=comment['comment_first']))
                    parent_comment_list = []
                    if len(parent_comment_list) == 0:
                        print 'Error, not foud parent comment for:', comment_second
                        pass
                    else:
                        # parent_comment = parent_comment_list[0]
                        # comment_second['parent_comment_id'] = parent_comment['comment_id']
                        comment_second['parent_comment_doctor_url'] = comment['comment_first']['doctor_url']
                        comment_second['parent_comment_comment_time'] = comment['comment_first']['comment_time']
                        comment_second['parent_comment_comment_content'] = comment['comment_first']['comment_content']
                        mysql.insert(table=comment_second_table_name, record=comment_second)
                        print '***二级评论已入库'
                        pass
            insert_doctor_url(doctor_url_list=post['post_like_doctor_url'],split_str=doctor_url_split,table_name=doctor_table_name,crawl_number=crawl_number,mysql=mysql,split=True)
            insert_doctor_url(doctor_url_list=post['post_comment_doctor_url'],split_str=doctor_url_split,table_name=doctor_table_name,crawl_number=crawl_number,mysql=mysql,split=True)
            insert_doctor_url(doctor_url_list=[post['post_doctor_url']],table_name=doctor_table_name,crawl_number=crawl_number,mysql=mysql)
        else:
            print '#### Error!!'
            file_error = open(file_path + error_url_file, 'a')
            error_writer = csv.writer(file_error)
            error_writer.writerow(line)
            file_error.close()
            error_number = error_number + 1
    file.close()
    mysql.close()
    end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print 'number of error urls:', error_number
    print 'start time:', start_time
    print 'end time:', end_time


def get_doctor_info(doctor_url_str,split_str,table_name,crawl_number):
    mysql = MySQLDatabaseClass()
    doctor_url_list = doctor_url_str.split(split_str)
    for url in doctor_url_list:
        if 'club.xywy.com/doc_card' in url:
            doctor = DoctorSpider(url=url,crawl_number=crawl_number)
            doctor_info = doctor.get_number()
            if doctor_info != None:
                mysql.insert(table=table_name,record=doctor_info)
                print '医生信息已入库',url
            else:
                pass

def insert_doctor_url(doctor_url_list,table_name, mysql,crawl_number,split = False,split_str=None):
    if split == True:
         doctor_url_list = doctor_url_list.split(split_str)
    else:
        pass
    for url in doctor_url_list:
        if 'club.xywy.com/doc_card' in url:
            doctor_info = {}
            doctor_info['doctor_url'] = url
            doctor_info['crawl_number'] = crawl_number
            print doctor_info
            mysql.insert(table=table_name, record=doctor_info)


def update_doctor_info(table_name,crawl_number):
    mysql = MySQLDatabaseClass()
    doctor_dict_list = mysql.select(table = table_name,record={'crawl_number':crawl_number})
    for doctor_dict in doctor_dict_list:
        url = doctor_dict['doctor_url']
        doctor = DoctorSpider(url=url, crawl_number=crawl_number)
        doctor_info = doctor.get_number()
        if doctor_info != None:
            mysql.update(table=table_name,record=doctor_info,primary_key={'doctor_url':url, 'crawl_number':doctor_dict['crawl_number']})
            print '医生信息已入库', url
        else:
            pass



if __name__ == '__main__':
    file_path = 'D:/Qianlong/PyCharmProjects/Crawler_xywy_doctor_communication/data/'
    help_topic_post_url_file = 'help_topic_url.csv'
    help_topic_post_url_error_file = 'help_topic_url_error.csv'
    post_table_name = 'help_topic_post'
    comment_first_table_name = 'help_topic_comment_first'
    comment_second_table_name = 'help_topic_comment_second'
    doctor_table_name = 'doctor_communication'
    doctor_url_split = '#####'
    afresh_post_url_file = False
    date_time = '2016-12-13'
    crawl_number = 1
    get_data(crawl_number=crawl_number,
                   data_path=file_path,
                   url_file=help_topic_post_url_file,
                   error_url_file=help_topic_post_url_error_file,
                   date_time=date_time,
                   post_table_name=post_table_name,
                   comment_first_table_name=comment_first_table_name,
                   comment_second_table_name = comment_second_table_name,
                   doctor_table_name = doctor_table_name,
                   doctor_url_split = doctor_url_split,
                   afresh_post_url_file = afresh_post_url_file)
    update_doctor_info('doctor_communication', crawl_number=crawl_number)
