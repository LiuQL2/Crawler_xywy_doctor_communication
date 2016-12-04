# usr/bin/env python
# -*- coding: utf-8 -*-

from classes.mysqlDatabaseClass import MySQLDatabaseClass
from spiders.GetPostUrl import GetPostUrl
from spiders.CaseSpider import CaseSpider
import csv

file_path = 'D:/Qianlong/PyCharmProjects/Crawler_xywy_doctor_communication/data/'
case_experience_post_url_file = 'case_experience_url.csv'
case_experience_post_url_file_got = 'case_experience_url_error.csv'

help_topic_post_url_file = 'help_topic_url-bakup.csv'
help_topic_post_url_file_got = 'help_topic_url_error.csv'

# case_experience = GetPostUrl(file_path=file_path,case_experience_name=case_experience_post_url_file,help_topic_name=help_topic_post_url_file)
# case_experience.get_case_experience_post_url()

file = open(file_path + case_experience_post_url_file,'r')
file_error = open(file_path + case_experience_post_url_file_got,'wb')
reader = csv.reader(file)
error_writer = csv.writer(file_error)

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
                parent_comment = (mysql.select(table='case_experience_comment_first', record=comment['comment_first']))[0]
                comment_second['parent_comment_comment_time'] = parent_comment['comment_time']
                comment_second['parent_comment_crawl_time'] = parent_comment['crawl_time']
                comment_second['parent_comment_content'] = parent_comment['comment_content']
                comment_second['parent_comment_doctor_url'] = parent_comment['doctor_url']
                mysql.insert(table='case_experience_comment_second', record=comment_second)
                print '***二级评论已入库'
                pass
    else:
        error_writer.writerow(line)

file.close()
file_error.close()
mysql.close()
