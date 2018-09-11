# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import os
class ImagesPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        image_url = item['image_link']
        yield Request(image_url)
    def item_completed(self, results, item, info):
        #results的第一个元素表示是否成功，第二个元素是个dict
        image_path = [x['path'] for ok, x in results if ok]
        #给文件重命名
        os.rename(self.IMAGES_STORE + '/' + image_path[0],\
                  self.IMAGES_STORE + '/' + item['nickname'] + '.jpg')
        item['image_path'] = self.IMAGES_STORE + '/' + item['nickname'] + '.jpg'
        return item
