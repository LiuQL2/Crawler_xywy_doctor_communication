#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
用来获取有问必答页面回答问题医生的信息。该板块医生分为三种类型，所以这里根据医生的网址形式进行分别处理。
"""

import datetime
import traceback
import re
import sys

from BaseSpider import BaseSpider
from database.MysqlDatabaseClass import MySQLDatabaseClass
from database.IOHandler import FileIO

reload(sys)
sys.setdefaultencoding('utf-8')


class GetAnswerDoctor(object):
    def __init__(self,url_table,answer_doctor_table,family_doctor_table, zhuanjia_doctor_table):
        self.url_table = url_table
        self.answer_doctor_table = answer_doctor_table
        self.family_doctor_table = family_doctor_table
        self.zhuanjia_doctor_table = zhuanjia_doctor_table
        self.doctor_url = list()
        pass

    def get_url(self):
        self.mysql = MySQLDatabaseClass()
        self.doctor_url = self.mysql.select(table=self.url_table)
        return self.doctor_url

    def get_doctor_info(self):
        for url in self.doctor_url:
            doctor_url = url['doctor_url']
            doctor = Doctor(url=doctor_url,answer_doctor_table=self.answer_doctor_table,family_doctor_table=self.family_doctor_table,
                            zhuanjia_doctor_table=self.zhuanjia_doctor_table,mysql = self.mysql)
            if 'family' in doctor_url:
                doctor.get_family_doctor()
                pass
            elif 'doc_card' in doctor_url:
                # doctor.get_answer_doctor()
                pass
            elif 'z.xywy.com/doc' in doctor_url:
                # doctor.get_zhuanjia_doctor()
                pass


class Doctor(BaseSpider):
    def __init__(self,url,answer_doctor_table,family_doctor_table, zhuanjia_doctor_table,mysql):
        self.url = url
        self.answer_doctor_table = answer_doctor_table
        self.family_doctor_table = family_doctor_table
        self.zhuanjia_doctor_table = zhuanjia_doctor_table
        self.mysql = mysql

    def get_answer_doctor(self,url=None):
        if url == None:
            sel = self.process_url_request(url=self.url, whether_decode=True, encode_type='GBK')
        else:
            sel = self.process_url_request(url=url, whether_decode=True, encode_type='GBK')
        mode = re.compile(r'\d+')
        doctor = {}
        doctor['doctor_url'] = self.url
        try:
            profile_list = sel.xpath('//ul[@class="fl bdul f14"]/li/span[2]/text()')
            doctor['name'] = profile_list[0]
            doctor['title'] = profile_list[1]
            doctor['department'] = profile_list[2]
            if len(sel.xpath('//ul[@class="bdxli pt10 f12 clearfix black"]/li/span/text()')) == 5:
                doctor['grade'] = sel.xpath('//ul[@class="bdxli pt10 f12 clearfix black"]/li[1]/span/text()')[0]
                doctor['best_reply'] = mode.findall(sel.xpath('//ul[@class="bdxli pt10 f12 clearfix black"]/li[2]/span/text()')[0])[0]
                doctor['help_user'] = mode.findall(sel.xpath('//ul[@class="bdxli pt10 f12 clearfix black"]/li[3]/span/text()')[0])[0]
                doctor['gratitude_user'] = \
                mode.findall(sel.xpath('//ul[@class="bdxli pt10 f12 clearfix black"]/li[5]/span/text()')[0])[0]
                doctor['fan'] = \
                mode.findall(sel.xpath('//ul[@class="bdxli pt10 f12 clearfix black"]/li[6]/span/text()')[0])[0]
                reputation_content = sel.xpath('//ul[@class="bdxli pt10 f12 clearfix black"]/li[4]/cite/img/@src')
                doctor['reputation_type'] = reputation_content[0].split('ysmp/')[1].replace('.gif','')
                doctor['reputation'] = len(reputation_content)
            else:
                pass
            doctor['skill'] = sel.xpath('//div[@class="clearfix cl djzhan f12 mr10 pt10 pb10 none"]/p/text()')[0].replace('擅长疾病：','')
            doctor['hospital'] = sel.xpath('//div[@class="clearfix cl djzhan f12 mr10 pt10 pb10 none"]/p/text()')[1].replace('所在医院：','')
            doctor['introduce'] = sel.xpath('//div[@class="clearfix cl djzhan f12 mr10 pt10 pb10 none"]/div/text()')[0].replace('个人简介：','')
            doctor['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d')
            print '================================================================='
            Doctor.print_doctor(doctor)
            self.mysql.insert(table=self.answer_doctor_table, record=doctor)
            return doctor
        except Exception, e:
            print traceback.format_exc(),e.message
            FileIO.exceptionHandler(traceback.format_exc(),url=self.url)
            FileIO.writeToFile(self.url,'./../data/answer_doctor_url_error.csv')
            return None

    def get_family_doctor(self,url=None):
        if url == None:
            sel = self.process_url_request(url=self.url, whether_decode=True, encode_type='GBK')
        else:
            sel = self.process_url_request(url=url, whether_decode=True, encode_type='GBK')
        mode = re.compile(r'\d+')
        doctor = {}
        doctor['doctor_url'] = self.url
        try:
            name = sel.xpath('//h3[@class="fn clearfix cl"]/i/text()')
            if len(name) == 1:
                doctor['name'] = name[0].replace('医生个人主页','')
                doctor['title'] = sel.xpath('//div[@class=" lh200 pt10 f14"]/text()')[0]
                doctor['hospital'] = sel.xpath('//div[@class=" lh200 pt10 f14"]/text()')[1].split('-')[0]
                doctor['department'] = sel.xpath('//div[@class=" lh200 pt10 f14"]/text()')[1].split('-')[1]
                doctor['skill'] = sel.xpath('//div[@class="clearfix"]/div[1][@class="HomeJie f14 fwei pt20"]/div/text()')[0]
                introduce = sel.xpath('//div[@class="clearfix"]/div[2][@class="HomeJie f14 fwei pt20"]/div/text()')
                if len(introduce) != 0:
                    doctor['introduce'] = introduce[0]
                else:
                    pass
                doctor['reputation'] = sel.xpath('//div[@class="clearfix mt20"]/span/text()')[0]
                help_content = sel.xpath('//div[@class="f14 fwei HomeHelp tc lh200 clearfix pt10"]/span/text()')
                if len(help_content) == 2:
                    doctor['help_user'] = sel.xpath('//div[@class="f14 fwei HomeHelp tc lh200 clearfix pt10"]/span/text()')[0]
                    doctor['sign'] = sel.xpath('//div[@class="f14 fwei HomeHelp tc lh200 clearfix pt10"]/span/text()')[1]
                else:
                    doctor['help_user'] = sel.xpath('//div[@class="f14 fwei HomeHelp tc lh200 clearfix pt10"]/span/text()')[0]
                doctor['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d')
            else:
                url = 'http://club.xywy.com/doc_card/' + self.url.split('/')[-1]
                self.url = url
                doctor = self.get_answer_doctor(url=url)
            Doctor.print_doctor(doctor)
            self.mysql.insert(table=self.family_doctor_table, record=doctor)
            return doctor
        except Exception,e:
            print traceback.format_exc(),e.message
            FileIO.exceptionHandler(traceback.format_exc(),url=self.url)
            FileIO.writeToFile(self.url,'./../data/answer_doctor_url_error.csv')
            return None

    def get_zhuanjia_doctor(self,url=None):
        if url == None:
            sel = self.process_url_request(url=self.url, whether_decode=True, encode_type='GBK')
        else:
            sel = self.process_url_request(url=url, whether_decode=True, encode_type='GBK')
        mode = re.compile(r'\d+')
        doctor = {}
        doctor['doctor_url'] = self.url
        try:
            doctor['name'] = sel.xpath('//h3[@class="fn"]/a/text()')[0].replace('专家网站','')
            doctor['title'] = sel.xpath('//div[@class="fl f12 lightblue-a lh200 pt5"]/p[2]/text()')[0].split(' ')[0]
            doctor['profession'] = sel.xpath('//div[@class="fl f12 lightblue-a lh200 pt5"]/p[2]/text()')[0].split(' ')[1]
            doctor['hospital'] = sel.xpath('//div[@class="fl f12 lightblue-a lh200 pt5"]/p[3]/a/text()')[0]
            doctor['department'] = sel.xpath('//div[@class="fl f12 lightblue-a lh200 pt5"]/p[4]/a/text()')[0]
            doctor['skill'] = sel.xpath('//div[@id="goodat"]/text()')[0].replace('擅长：','')
            doctor['introduce'] = sel.xpath('//div[@id="person_info"]/text()')[0].replace('简介：','')
            doctor['help_user'] = sel.xpath('//div[@class=" f12 padd10 lh30"]/span[4]/a/text()')[0]
            doctor['good_comment'] = sel.xpath('//div[@class=" f12 padd10 lh30"]/span[5]/a/text()')[0]
            doctor['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d')
            Doctor.print_doctor(doctor)
            self.mysql.insert(table=self.zhuanjia_doctor_table, record=doctor)
            return doctor
        except Exception,e:
            print traceback.format_exc(),e.message
            FileIO.exceptionHandler(traceback.format_exc(),url=self.url)
            FileIO.writeToFile(self.url,'./../data/answer_doctor_url_error.csv')
            return None

    @staticmethod
    def print_doctor(doctor):
        for (key, value) in doctor.items():
            print key,':', value



if __name__ == '__main__':
    get_doctor = GetAnswerDoctor(url_table='2016_doctor_url', answer_doctor_table='2016_doctor_info_answer',
                                 family_doctor_table='2016_doctor_info_family', zhuanjia_doctor_table='2016_doctor_info_zhuanjia')
    get_doctor.get_url()
    get_doctor.get_doctor_info()

    # doctor = Doctor('http://z.xywy.com/doc/zyz8872/')
    # # doctor.get_family_doctor()
    # doctor.get_zhuanjia_doctor()