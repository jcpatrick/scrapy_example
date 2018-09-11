# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class ScrapydemoPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json

class ItcastPipeline(object):
    def __init__(self):
        #初始化，可选
        self.f = open("teacher.json", 'w', encoding='utf-8')
    #必须要有的，接收和处理item
    def process_item(self, item, spider):
        jsonstr = json.dumps(dict(item), ensure_ascii=False)
        self.f.write(jsonstr+"\n")
    #可选的，结束时调用
    def close_spider(self,spider):
        self.f.close()