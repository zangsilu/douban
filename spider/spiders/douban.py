# -*- coding: utf-8 -*-
import scrapy
from spider.doubanItem import DoubanItem

class Douban(scrapy.Spider):
    name = 'douban'
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for info in list:
            item = DoubanItem()
            item['title'] = info.xpath('.//div/div[2]/div[1]/a/span[1]/text()').extract_first()
            item['intro'] = info.xpath('.//div/div[2]/div[2]/p[1]/text()').extract_first().replace(' ','').replace('\n','')
            item['imageUrl'] = info.xpath('.//div/div[1]/a/img/@src').extract_first()
            item['desc'] = info.xpath('.//div/div[2]/div[2]/p[2]/span/text()').extract_first()
            item['star'] = info.xpath('.//div/div[2]/div[2]/div/span[2]/text()').extract_first()
            item['commentCount'] = info.xpath('.//div/div[2]/div[2]/div/span[4]/text()').extract_first()
            yield item

        nextPage = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()
        if nextPage:
            url = response.urljoin(nextPage)
            yield scrapy.Request(url,self.parse)