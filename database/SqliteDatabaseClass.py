#!/usr/bin/env python
# -*-coding: utf-8 -*-

'''
用来读取sqlite数据库中的文件。
'''

# Author: Liu Qianlong <LiuQL2@163.com>
# Date: 2016.10.24


import sys
import sqlite3
from database.MysqlDatabaseClass import MySQLDatabaseClass

reload(sys)
sys.setdefaultencoding('utf-8')


class SQLiteDatabaseClass(object):

    def __init__(self, file_path):
        """
        初始化一个实例。
        :param file_path: sqlite数据库文件的路径需要确定到文件名称，如：'D:/Qianlong/Liuan/xywy.db3'。
        """
        self.file_path = file_path
        self.__connection = None
        self.__cursor = None

    def connect(self):
        """
        连接sqlite数据库文件。
        :return: 不返回数据。
        """
        self.__connection = sqlite3.connect(database=self.file_path)

    def select(self, table, size = None):
        """
        数据库中读取操作。
        :param table: 需要读取数据的表名，不能为空。
        :param size: 需要返回数据的数量，100表示返回100条记录，可以为空，表示返回表table中的全部数据。
        :return: 返回查询数据的结果。
        """
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute('select * from '+ table + ';')
        if size == None:
            data_tuple = self.__cursor.fetchall()
        else:
            data_tuple = self.__cursor.fetchmany(size=size)
        self.__cursor.close()
        return self.__tuple_to_dict__(data_tuple, table= table)

    def table_info(self,table):
        """
        用于表结构的查询操作。
        :param table: 需要查询的表，不能为空。
        :return: 返回表的结构。
        """
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute('PRAGMA table_info('+ table +');')
        info = self.__cursor.fetchall()
        self.__cursor.close()
        return info

    def table_column(self, table):
        table_info = self.table_info(table = table)
        column_name = []
        for column in table_info:
            column_name.append(column[1])
        return column_name

    def __tuple_to_dict__(self, data, table):
        data_list = []
        table_column = self.table_column(table=table)
        for line in data:
            record = {}
            for index in range(0, len(table_column), 1):
                record[table_column[index]] = line[index]
            data_list.append(record)
        return data_list

    def close(self):
        """
        关闭数据库的连接。
        :return: 无返回数据。
        """
        self.__connection.close()



if __name__ == '__main__':
    database = SQLiteDatabaseClass('D:/Qianlong/Liuan/xywy.db3')
    database.connect()
    values = database.select(table='Content_en',size=100)
    for record in values:
        print record
    print database.table_info(table='Content_en')
    print database.table_column(table='Content_en')
    print type(values), type(values[2])
    print len(values)
    database.close()