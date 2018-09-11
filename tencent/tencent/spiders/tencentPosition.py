# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentPositionItem
import re

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    offset = 0
    start_urls = ['https://hr.tencent.com/position.php?&start=' + str(offset), ]

    def parse(self, response):
        # //tr[@class="even"or@class="odd"]
        for each in response.xpath('//tr[@class="even"or@class="odd"]'):
            item = TencentPositionItem()
            name = each.xpath('./td[1]/a/text()').extract()
            link = each.xpath('./td[1]/a/@href').extract()
            position_type = each.xpath('./td[2]/text()').extract()
            people_num = each.xpath('./td[3]/text()').extract()
            work_location = each.xpath('./td[4]/text()').extract()
            publish_time = each.xpath('./td[5]/text()').extract()
            if len(name) > 0:
                item['position_name'] = name[0]
            else:
                item['position_name'] = ""
            if len(link) > 0:
                item['position_link'] = link[0]
            else:
                item['position_link'] = ""
            if len(position_type) > 0:
                item['position_type'] = position_type[0]
            else:
                item['position_type'] = ""
            if len(people_num) > 0:
                item['people_num'] = people_num[0]
            else:
                item['people_num'] = ""
            if len(work_location) > 0:
                item['work_location'] = work_location[0]
            else:
                item['work_location'] = ""
            if len(publish_time) > 0:
                item['publish_time'] = publish_time[0]
            else:
                item['publish_time'] = ""
            yield item
        if self.offset < 3500:
            self.offset += 10
        request_url = re.sub('\d+', str(self.offset), response.url)
        yield scrapy.Request(request_url, callback=self.parse)
