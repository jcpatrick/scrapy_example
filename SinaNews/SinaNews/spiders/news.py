# -*- coding: utf-8 -*-
import scrapy
import os
from SinaNews.items import SinanewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):

        for each in response.xpath('//div[@id="tab01"]/div'):
            #获取大类标题
            parent_title = each.xpath('./h3/a/text()').extract()[0]
            parent_url = each.xpath('./h3/a/@href').extract()[0]
            parent_file_name = './Data/' + parent_title
            if not os.path.exists(parent_file_name):
                os.makedirs(parent_file_name)

            #获取小类标题
            for sub in each.xpath('./ul/li'):
                item = SinanewsItem()
                sub_url = sub.xpath('./a/@href').extract()[0]
                sub_title = sub.xpath('./a/text()').extract()[0]
                sub_filename = parent_file_name + '/' + sub_title
                if not os.path.exists(sub_filename):
                    os.makedirs(sub_filename)
                item['parent_title'] = parent_title
                item['parent_url'] = parent_url
                item['sub_title'] = sub_title
                item['sub_url'] = sub_url
                item['sub_filename'] = sub_filename
                yield scrapy.Request(url=sub_url, meta={'item1': item}, callback=self.parse_sub)

    def parse_sub(self, response):
        meta_1 = response.meta['item1']
        son_urls = response.xpath("//a/@href").extract()
        for i in range(0, len(son_urls)):
            url = son_urls[i]
            if url.endswith('.shtml'): #and url.startswith(meta_1['parent_url']):
                item = SinanewsItem()
                item['parent_title'] = meta_1['parent_title']
                item['parent_url'] = meta_1['parent_url']
                item['sub_title'] = meta_1['sub_title']
                item['sub_url'] = meta_1['sub_url']
                item['sub_filename'] = meta_1['sub_filename']
                item['son_url'] = url
                yield scrapy.Request(url, meta={'meta_2': item}, callback=self.parse_son_detail)
    def parse_son_detail(self, response):
        item = response.meta['meta_2']
        content = ''
        #标题
        #//h1[@class="main-title"]
        head = response.xpath('//h1[@class="main-title"]/text()')
        #内容
        #//div[@id="artibody" or @id="article"]//p/text()
        content_list = response.xpath('//div[@id="artibody" or @id="article"]//p/text()').extract()

        for content_p in content_list:
            content += content_p

        item['head'] = head
        item['content'] = content
        yield item