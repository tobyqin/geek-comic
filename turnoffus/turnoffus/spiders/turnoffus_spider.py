import json
import re
from os.path import dirname, join

import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ..settings import USE_SELENIUM

HOST = 'http://turnoff.us'
save_file = join(dirname(dirname(dirname(__file__))), 'turnoffus.json')


class TurnoffusSpider(scrapy.Spider):
    name = "turnoffus"
    data = []

    def start_requests(self):
        urls = [
            'http://turnoff.us/all/'
        ]
        for url in urls:
            if USE_SELENIUM:
                yield SeleniumRequest(url=url,
                                      callback=self.parse_result,
                                      wait_time=10,
                                      wait_until=EC.visibility_of_element_located((By.XPATH, "//article/p/img")))
            else:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse_result(self, response):
        """selenium parser"""
        print("================================")
        print(response.selector.xpath('//h1[@class="post-title"]/text()'))
        print(response.selector.xpath("//article/p/img"))
        print("================================")

    def parse(self, response):
        img = response.xpath("//article/p/img/@src").get()
        if img:
            header = response.xpath('//h1[@class="post-title"]/text()').get()
            img_src = response.xpath("//article/p/img/@src").get()
            title = self.build_img_name(header, img_src)
            img_src = self.build_img_src(img_src)
            self.data.append({
                "title": header,
                "name": title,
                "src": img_src
            })
            self.save_output()
        else:
            all_posts = response.xpath("//h2/a/@href").getall()
            for post in all_posts:
                url = HOST + post
                yield scrapy.Request(url=url, callback=self.parse)

    def build_img_name(self, name, src):
        name = re.sub("[^\w\d]+", "-", name)[1:]
        name = re.sub("[^\w\d]+$", "", name)
        name = re.sub("^[^\w\d]+", "", name) + src[-4:]
        return name

    def build_img_src(self, src):
        return HOST + src

    def save_output(self):
        with open(save_file, mode='w', encoding='utf8') as f:
            f.write(json.dumps(self.data, indent=2))
