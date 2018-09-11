# -*- coding: utf-8 -*-
import scrapy
from Douyu.items import DouyuItem
import json
class DouyumeinvSpider(scrapy.Spider):
    name = 'douyumeinv'
    allowed_domains = ['capi.douyucdn.cn']
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [url + str(offset), ]

    def parse(self, response):
        content = response.text
        data = json.loads(content)['data']
        for each in data:
            item = DouyuItem()

            item['nickname'] = each['nickname']
            item['image_link'] = each['vertical_src']
            yield item
        #如果当前页的长度小于每页20的数量，说明当前已经是最后一页了，就停止
        if len(data) == 20:
            self.offset += 20
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

