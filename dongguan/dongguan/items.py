# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    title = scrapy.Field()
    code = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    text_pic = scrapy.Field()
