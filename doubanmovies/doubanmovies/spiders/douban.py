# -*- coding: utf-8 -*-
import scrapy
from doubanmovies.items import DoubanmoviesItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    offset = 0
    base_url = 'https://movie.douban.com/top250?start='
    start_urls = [base_url + str(offset) + '&filter=']

    def parse(self, response):
        for each in response.xpath('//div[@class="info"]'):
            # 标题：.//span[@class="title"][1]/text()
            title = each.xpath('.//span[@class="title"][1]/text()').extract()[0]
            #//p[1]/text()
            bd = each.xpath('.//p[1]/text()').extract()
            #//span[@class="rating_num"]/text()
            star = each.xpath('.//span[@class="rating_num"]/text()').extract()[0]
            #//span[@class="inq"]//text()
            quote = each.xpath('.//span[@class="inq"]//text()').extract()

            item = DoubanmoviesItem()
            item['title'] = title
            item['star'] = star
            item['bd'] = bd
            if len(quote) > 0:
                item['quote'] = quote[0]
            yield item

        if self.offset < 250:
            self.offset += 25
            url = self.base_url + str(self.offset) + '&filter='
            yield scrapy.Request(url)
