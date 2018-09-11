# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmoviesItem(scrapy.Item):
    title = scrapy.Field()
    star = scrapy.Field()
    bd = scrapy.Field()
    quote = scrapy.Field()
