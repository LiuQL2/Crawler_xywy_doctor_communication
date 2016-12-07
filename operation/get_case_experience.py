# usr/bin/env python
# -*- coding: utf-8 -*-

from classes.mysqlDatabaseClass import MySQLDatabaseClass
from spiders.GetPostUrl import GetPostUrl
from spiders.CaseSpider import CaseSpider
import csv
import datetime
import time

file_path = 'D:/Qianlong/PyCharmProjects/Crawler_xywy_doctor_communication/data/'
case_experience_post_url_file = 'case_experience_url.csv'
case_experience_post_url_file_got = 'case_experience_url_error.csv'

help_topic_post_url_file = 'help_topic_url-bakup.csv'
help_topic_post_url_file_got = 'help_topic_url_error.csv'
start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
case_experience = GetPostUrl(file_path=file_path,case_experience_name=case_experience_post_url_file,help_topic_name=help_topic_post_url_file)
case_experience.get_case_experience_post_url()

while True:
    crawl_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if '2016-12-07' in crawl_time:
        break
    else:
        time.sleep(1)
        print 'waiting', crawl_time
        pass

file = open(file_path + case_experience_post_url_file,'r')
reader = csv.reader(file)
file_error = open(file_path + case_experience_post_url_file_got,'wb')
error_writer = csv.writer(file_error)
file_error.close()
error_number = 0
mysql = MySQLDatabaseClass()
for line in reader:
    print line[0],'********************************************************************************************************************************************'
    spider = CaseSpider(line[0])
    post_comment = spider.parse()
    if post_comment != False:
        post = post_comment['post']
        comment_list = post_comment['comment_list']
        mysql.insert(table = 'case_experience_post',record=post)
        print '***帖子信息已入库'
        index = 1
        for comment in comment_list:
            mysql.insert(table='case_experience_comment_first', record=comment['comment_first'])
            print '***第', str(index),'个一级评论已入库'
            index = index + 1
            for comment_second in comment['comment_second_list']:
                # comment_second['parent_comment_comment_time'] = parent_comment['comment_time']
                # comment_second['parent_comment_crawl_time'] = parent_comment['crawl_time']
                # comment_second['parent_comment_content'] = parent_comment['comment_content']
                # comment_second['parent_comment_doctor_url'] = parent_comment['doctor_url']
                parent_comment_list = (mysql.select(table='case_experience_comment_first', record=comment['comment_first']))
                if len(parent_comment_list) == 0:
                    print 'Error, not foud parent comment for:', comment_second
                    pass
                else:
                    parent_comment = parent_comment_list[0]
                    comment_second['parent_comment_id'] = parent_comment['comment_id']
                    mysql.insert(table='case_experience_comment_second', record=comment_second)
                    print '***二级评论已入库'
                    pass
    else:
        file_error = open(file_path + case_experience_post_url_file_got, 'a+')
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
