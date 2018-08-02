# -*- coding: utf-8 -*-

import scrapy

class DoubanItem(scrapy.Item):
    imageUrl = scrapy.Field()
    intro = scrapy.Field()
    commentCount = scrapy.Field()
    desc = scrapy.Field()
    star = scrapy.Field()
    title = scrapy.Field()
