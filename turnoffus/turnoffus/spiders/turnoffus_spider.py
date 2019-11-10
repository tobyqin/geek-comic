import scrapy
import re

from scrapy_selenium import SeleniumRequest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ..settings import USE_SELENIUM

HOST = 'http://turnoff.us'


class TurnoffusSpider(scrapy.Spider):
    name = "turnoffus"

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
                yield scrapy.Request(url=url, callback=self.parse_index)

    def parse_result(self, response):
        """selenium parser"""
        print("================================")
        print(response.selector.xpath('//h1[@class="post-title"]/text()'))
        print(response.selector.xpath("//article/p/img"))
        print("================================")

    def parse_index(self, response):

        img = response.xpath("//article/p/img/@src").get()
        if img:
            title = response.xpath('//h1[@class="post-title"]/text()').get()
            img_src = response.xpath("//article/p/img/@src").get()
            title = self.build_img_name(title, img_src)
            img_src = self.build_img_src(img_src)
            print(title)
            print(img_src)

        all_posts = response.xpath("//h2/a/@href").getall()
        print(all_posts)
        for post in all_posts[1:5]:
            url = HOST + post
            yield scrapy.Request(url=url, callback=self.parse_index)

    def parse_post(self, response):
        """default parser"""
        print("================================")
        title = response.xpath('//h1[@class="post-title"]/text()').get()
        img_src = response.xpath("//article/p/img/@src").get()
        title = self.build_img_name(title, img_src)
        img_src = self.build_img_src(img_src)
        print(title)
        print(img_src)
        print("================================")

    def build_img_name(self, name, src):
        name = re.sub("[^\w\d]+", "-", name)[1:]
        name = re.sub("^[^\w\d]+", "", name) + src[-4:]
        return name

    def build_img_src(self, src):
        return HOST + src
