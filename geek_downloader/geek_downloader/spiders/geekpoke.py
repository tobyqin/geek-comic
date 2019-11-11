# -*- coding: utf-8 -*-
import scrapy


class GeekpokeSpider(scrapy.Spider):
    name = 'geekpoke'
    allowed_domains = ['http://geek-and-poke.com/']
    start_urls = ['http://http://geek-and-poke.com//']

    def parse(self, response):
        pass
