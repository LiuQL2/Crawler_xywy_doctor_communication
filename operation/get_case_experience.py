# usr/bin/env python
# -*- coding: utf-8 -*-

from GetInsertDatabase import GetData

if __name__ == '__main__':
    file_path = 'D:/Qianlong/PyCharmProjects/Crawler_xywy_doctor_communication/data/'
    url_file = 'case_experience_url.csv'
    error_url_file = 'case_experience_url_error.csv'
    sucess_url_file = 'case_experience_url_sucess.csv'
    post_table_name = 'case_experience_post'
    comment_first_table_name = 'case_experience_comment_first'
    comment_second_table_name = 'case_experience_comment_second'
    doctor_table_name = 'doctor_communication'
    doctor_url_only_table_name = 'doctor_url'
    doctor_url_split = '#####'
    date_time = '2016-12-22'
    afresh_post_url_file = True
    crawl_number = 1
    post_type = 'case_experience'

    get_data = GetData(crawl_number=crawl_number,
                       data_path=file_path,
                       url_file=url_file,
                       error_url_file=error_url_file,
                       success_url_file=sucess_url_file,
                       date_time=date_time,
                       post_table_name=post_table_name,
                       comment_first_table_name=comment_first_table_name,
                       comment_second_table_name = comment_second_table_name,
                       doctor_table_name = doctor_table_name,
                       doctor_url_only_table_name=doctor_url_only_table_name,
                       post_type=post_type,
                       doctor_url_split = doctor_url_split,
                       afresh_post_url_file = afresh_post_url_file)
    get_data.get_data()
    get_data.update_doctor_info()
    get_data.close_database()
    get_data.process_info()