#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from spiders.GetPostUrl import GetPostUrl
reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    file_path = 'D:/Qianlong/PyCharmProjects/Crawler_xywy_doctor_communication/data/'
    case_experience_post_url_file = 'case_experience_url.csv'
    help_topic_post_url_file = 'help_topic_url.csv'

    # help_topic = GetPostUrlThread(file_path=file_path,case_experience_name=case_experience_post_url_file,help_topic_name=help_topic_post_url_file,run_type='help_topic')
    # help_topic.start()
    # help_topic.join()
    # case_experience = GetPostUrlThread(file_path=file_path,case_experience_name=case_experience_post_url_file,help_topic_name=help_topic_post_url_file,run_type='case_topic')
    # case_experience.start()
    # case_experience.join()

