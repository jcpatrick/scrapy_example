# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
import json
import logging
class DoubanmoviesPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        user = settings['MONGODB_USER']
        password = settings['MONGODB_PASSWD']
        db_name = settings['MONGODB_DB_NAME']
        sheet_name = settings['MONGODB_SHEET_NAME']
        mongo_url = "mongodb://" + user + ":" + password + "@" + host + ":" + port + "/" + db_name
        logging.debug(mongo_url)
        self.client = pymongo.MongoClient(mongo_url)

        db = self.client['py_test']
        self.sheet = db[sheet_name]

    def process_item(self, item, spider):

        data = dict(item)
        self.sheet.insert_one(data)
        return item
    def close_spider(self, spider):
        self.client.close()