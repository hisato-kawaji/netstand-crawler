# -*- coding: utf-8 -*-

import json
import os
import psycopg2
import codecs


class NetstandCrawlerPipeline(object):

    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.environ.get('NETSTAND_DB_HOST'),
            port=os.environ.get('NETSTAND_DB_PORT'),
            dbname=os.environ.get('NETSTAND_DB_NAME'),
            user=os.environ.get('NETSTAND_DB_USER'),
            password=os.environ.get('NETSTAND_DB_PASSWORD')
        )
        self.cur = self.connection.cursor()
        self.file = codecs.open('list.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        title = dict(item)['title']
        url = dict(item)['url']
        self.cur.execute(
            "INSERT INTO links VALUES(nextval('links_id_seq'), 1, %s, %s, NOW(), NOW())",
            [title, url]
        )
        self.connection.commit()
        return item

    def spider_closed(self, spider):
        self.file.close()
        self.cur.close()
