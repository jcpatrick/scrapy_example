# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinanewsItem(scrapy.Item):
    #大类的标题和url
    parent_title = scrapy.Field()
    parent_url = scrapy.Field()
    #小类的标题和url和文件路径
    sub_title = scrapy.Field()
    sub_url = scrapy.Field()
    sub_filename = scrapy.Field()

    #小类下面的所有子页面的路径
    son_url = scrapy.Field()
    #文章的标题和内容
    head = scrapy.Field()
    content = scrapy.Field()
