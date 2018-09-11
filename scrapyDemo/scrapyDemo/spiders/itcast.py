# -*- coding: utf-8 -*-
import scrapy
from scrapyDemo.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = [
        'http://www.itcast.cn/channel/teacher.shtml#ajavaee',
        'http://www.itcast.cn/channel/teacher.shtml#ac',
        'http://www.itcast.cn/channel/teacher.shtml#acloud',
        'http://www.itcast.cn/channel/teacher.shtml#ads',
        'http://www.itcast.cn/channel/teacher.shtml#ago',
        'http://www.itcast.cn/channel/teacher.shtml#aLinux',
        'http://www.itcast.cn/channel/teacher.shtml#amovies',
        'http://www.itcast.cn/channel/teacher.shtml#anetmarket',
        'http://www.itcast.cn/channel/teacher.shtml#aphp',
        'http://www.itcast.cn/channel/teacher.shtml#apm',
        'http://www.itcast.cn/channel/teacher.shtml#apython',
        'http://www.itcast.cn/channel/teacher.shtml#atest',
        'http://www.itcast.cn/channel/teacher.shtml#aui',
        'http://www.itcast.cn/channel/teacher.shtml#auijp',
        'http://www.itcast.cn/channel/teacher.shtml#aweb',
    ]

    def parse(self, response):
        for each in response.xpath('//div[@class="li_txt"]'):
            item = ItcastItem()

            name = each.xpath('./h3/text()').extract()
            level = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()

            item['name'] = name[0]
            item['level'] = level[0]
            item['info'] = info[0]
            yield item
