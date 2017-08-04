# /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time

from database.RabbitMQ import RabbitmqConsumer
from database.RabbitMQ import RabbitmqServer
from configuration.settings import CRAWL_NUMBER as crawl_number
from configuration.settings import POST_INFO_QUEUE_EXCHANGE as post_info_queue_exchange
from configuration.settings import POST_URL_QUEUE_EXCHANGE as post_url_queue_exchange
from configuration.settings import TIME_SLEEP as time_sleep


class PostUrlConsumer(RabbitmqConsumer):
    """
    将抓取到并保存在rabbitmq服务器中的post_url读取出获取post详细内容
    """
    def __init__(self,queue, queue_durable):
        super(PostUrlConsumer,self).__init__(queue=queue,queue_durable=queue_durable)

    def callback(self,ch,method,properties, body):
        body = json.loads(body)
        if body['type'] == 'case_experience':
            from spiders.CaseSpider import CaseSpider
            spider = CaseSpider(url=body['content'],crawl_number=crawl_number)
            post_comment = spider.parse()
            pass
        else:
            from spiders.HelpSpider import HelpSpider
            spider = HelpSpider(url=body['content'],crawl_number=crawl_number)
            post_comment = spider.parse()
        #如果失败重新放回该队列，等待下一次处理
        if post_comment==None:
            RabbitmqServer.add_message(message=json.dumps(body),
                                       routing_key=post_url_queue_exchange['routing_key'],
                                       queue=post_url_queue_exchange['queue'],
                                       queue_durable=post_url_queue_exchange['queue_durable'],
                                       exchange=post_url_queue_exchange['exchange'],
                                       exchange_type=post_url_queue_exchange['exchange_type'])
            pass
        #获取到的post存入post_info队列中，准备入库
        else:
            message = {}
            message['type'] = body['type']
            message['content'] = json.dumps(post_comment)
            RabbitmqServer.add_message(message=json.dumps(message),
                                       routing_key=post_info_queue_exchange['routing_key'],
                                       queue=post_info_queue_exchange['queue'],
                                       queue_durable=post_info_queue_exchange['queue_durable'],
                                       exchange=post_info_queue_exchange['exchange'],
                                       exchange_type=post_info_queue_exchange['exchange_type'])
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print 'sleeping...'
        self.connection.sleep(time_sleep)



if __name__ == '__main__':
    consumer = PostUrlConsumer(queue=post_url_queue_exchange['queue'],
                                queue_durable=post_url_queue_exchange['queue_durable'])
    consumer.start_consuming()