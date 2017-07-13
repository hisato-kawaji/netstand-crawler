# -*- coding: utf-8 -*-
import scrapy


class NetstandCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()

    def __unicode__(self):
        return repr(self).decode('unicode_escape')
    pass
