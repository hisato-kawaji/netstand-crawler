# -*- coding: utf-8 -*-
import scrapy
from netstand_crawler.items import NetstandCrawlerItem


class HimasokuSpider(scrapy.Spider):
    name = "himasoku"
    allowed_domains = ["himasoku.com"]
    start_urls = (
        'http://himasoku.com/',
    )

    def parse(self, response):
        keys = response.xpath(
            '//div[@class="plugin-recent_articles sidewrapper"]/div[@class="side"]/div/a/text()'
        ).extract()
        values = response.xpath(
            '//div[@class="plugin-recent_articles sidewrapper"]/div[@class="side"]/div/a/@href'
        ).extract()
        for k, v in dict(zip(keys, values)).items():
            item = NetstandCrawlerItem()
            item['title'] = k
            item['url'] = v
            yield item
