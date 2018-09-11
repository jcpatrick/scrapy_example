# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinanewsPipeline(object):
    def process_item(self, item, spider):
        son_url = item['son_url']
        filename = son_url[7:-6].replace('/', '_')
        filename += ".txt"

        fp = open(item['sub_filename'] + '/' + filename, 'w', encoding='utf-8')
        fp.write(item['content'])
        fp.close()
        return item
