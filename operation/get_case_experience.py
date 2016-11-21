# usr/bin/env python
# -*- coding: utf-8 -*-

from classes.mysqlDatabaseClass import MySQLDatabaseClass
from spiders.GetPostUrl import GetPostUrl
from spiders.CaseSpider import CaseSpider
import csv

file_path = 'D:\Qianlong\PyCharmProjects\Crawler\data\\'
case_experience_post_url_file = 'case_experience_url.csv'
case_experience_post_url_file_got = 'case_experience_url_got.csv'
help_topic_post_url_file = 'case_experience_url.csv'
help_topic_post_url_file_got = 'case_experience_url_got.csv'
# case_experience = GetPostUrl(file_path=file_path,case_experience_name=case_experience_post_url_file,help_topic_name=help_topic_post_url_file)
# case_experience.get_case_experience_post_url()

file = open(file_path + case_experience_post_url_file,'r')
file_got = open(file_path + case_experience_post_url_file_got,'wb')
reader = csv.reader(file)
writer = csv.writer(file_got)

mysql = MySQLDatabaseClass()
for line in reader:
    print line[0],'********************************************************************************************************************************************'
    spider = CaseSpider(line[0])
    post_comment = spider.parse()
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
            parent_id = (mysql.select(table='case_experience_comment_first', record=comment['comment_first']))[0]['comment_id']
            comment_second['parent_comment_id'] = parent_id
            mysql.insert(table='case_experience_comment_second', record=comment_second)
            pass
        print '***二级评论已入库'
    writer.writerow(line)

file.close()
file_got.close()
mysql.close()
