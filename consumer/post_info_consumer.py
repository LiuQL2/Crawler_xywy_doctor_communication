# /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
from database.RabbitMQ import RabbitmqConsumer
from operation.GetInsertDatabase import InsertDatabase
from configuration.settings import POST_INFO_QUEUE_EXCHANGE as post_info_queue_exchange
from configuration.settings import DOCTOR_URL_SPLIT as doctor_url_split
from configuration.settings import CRAWL_NUMBER as crawl_number


class PostInfoConsumer(RabbitmqConsumer):
    """
    将抓取到并保存在rabbitmq服务器中的post_info进行入库操作
    """
    def __init__(self,queue, queue_durable):
        super(PostInfoConsumer,self).__init__(queue=queue,queue_durable=queue_durable)

    def callback(self,ch,method,properties, body):
        body = json.loads(body)
        insertData = InsertDatabase(message=body,doctor_url_split=doctor_url_split,crawl_number=crawl_number)
        insertData.process()
        insertData.close()
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print 'sleeping...'
        self.connection.sleep(0.5)


if __name__ == '__main__':
    consumer = PostInfoConsumer(queue=post_info_queue_exchange['queue'],
                                queue_durable=post_info_queue_exchange['queue_durable'])
    consumer.start_consuming()