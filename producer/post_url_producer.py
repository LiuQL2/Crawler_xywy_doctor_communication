# /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import time
import datetime
import os
import traceback
from spiders.GetPostUrl import GetPostUrl
from operation.GetInsertDatabase import InsertDatabase
from database.RabbitMQ import RabbitmqServer
from configuration.settings import POST_INFO_QUEUE_EXCHANGE as post_info_queue
from configuration.settings import POST_URL_QUEUE_EXCHANGE as post_url_queue

reload(sys)
sys.setdefaultencoding('utf-8')

def get_queues():
    """
    获取rabbitmq中的队列及其队列中消息的数量
    :return:
    """
    output = os.popen("rabbitmqctl list_queues")
    message = output.read()
    queues = dict()
    queues_list = message.split('\n')
    queues_list.pop(0)
    queues_list.pop()
    for element in queues_list:
        queue_name = element.split('\t')[0]
        message_number = int(element.split('\t')[1])
        queues[queue_name] = message_number
    return queues


#获取post的url
RabbitmqServer.queue_delete("post_url_queue")
spider = GetPostUrl()
spider.get_post_url()
#当所有的post都处理完毕且入库之后进行更新医生信息
temp_time = time.time()
temp_queue = {}
while True:
    try:
        queues = get_queues()
        project_queue = {}
        project_queue[post_url_queue['queue']] = queues[post_url_queue['queue']]
        project_queue[post_info_queue['queue']] = queues[post_info_queue['queue']]
        if queues[post_info_queue['queue']] == 0 and queues[post_url_queue['queue']] == 0:
            InsertDatabase.update_doctor_info()
            print 'Information of doctor have been updated.'
            break
        else:
            print queues
            if (time.time()-temp_time) > float(3600) and temp_queue != project_queue:
                temp_time = time.time()
                temp_queue = project_queue
            elif (time.time() - temp_time) > float(3600) and temp_queue == project_queue:
                InsertDatabase.update_doctor_info()
                print "information of doctor have been updated."
                break
            else:
                pass
    except Exception,e:
        print traceback.format_exc(),e.message
