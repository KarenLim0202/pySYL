# -*- coding: utf-8 -*-
import scrapy


class SylgitspiderSpider(scrapy.Spider):
    name = 'sylgitspider'
   # allowed_domains = ['github.com']
   # start_urls = ['http://github.com/']
mport scrapy

    @property
    def start_urls(self):
        url_tmpl="https://github.com/shiyanlou?page={}&tab=repositories"
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        item=SylgitItem({
            'name':response.css('div.mb-1 a::text').extract(),
            'update_time':response.css('div.mt-2 relative-time::attr(datetime)').extract()
            })
        yield item
