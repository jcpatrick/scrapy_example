# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem
import logging
class DongdongSpider(CrawlSpider):
    name = 'dongdong'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?ype=4',]

    rules = (
        Rule(LinkExtractor(allow='type=4'), process_links='modify_links'),
        Rule(LinkExtractor(allow=r'/question/\d+/\d+.shtml'), callback='parse_item', follow=True),
    )
    def modify_links(self, links):
        '''修改url连接，因为网站对url进行了转成，需修改成正确的格式
        网站抓去的url格式：xxxxType&type=4?page=xx
        实际可以访问的url格式:xxxxType?type=4&page=xx
        '''
        for link in links:
            link.url = link.url.replace('?', '&').replace('Type&', 'Type?')
        return links
    def parse_item(self, response):
        item = DongguanItem()
        title_block = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0]
        title_list = title_block.split(u"\xa0\xa0")#html的空格转成unicode之后变成了\xa0了，所以需要通过这种方式分隔
        # logging.debug(title_list)
        title = title_list[0].split('：')[1]
        code = title_list[1].split(':')[1]
        # logging.debug(title, code)

        #content可能会出现有图片的情况
        #有图片，则匹配contentext，没有则匹配c1 text14_2
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        if len(content) == 0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
        content = ''.join(content)
        content = content.replace('  ', '')
        # logging.debug(content)

        url = response.url

        item['title'] = title if title else ''
        item['content'] = content if content else ''
        item['url'] = url if url else ''
        item['code'] = code if code else ''

        yield item
