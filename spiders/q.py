# -*- coding: utf-8 -*-
import scrapy
from db.items import  DbItem

class QSpider(scrapy.Spider):
    name = 'q'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = "https://movie.douban.com/top250?start="
    start_urls = {
        url + str(offset),
    }

    def parse(self, response):

        item = DbItem()
        movie = response.xpath("//div[@class = 'item']")
        #  迭代获取每一块的信息
        for each in movie:
            #   标题
            item['title'] = each.xpath(".//div[@class ='info']//span[@class ='title'][1]/text()").extract()[0]
            #   信息
            bd=  each.xpath(".//div[@class ='info']//div[@class ='bd']/p/text()").extract()[0]
            item['bd'] = "".join(bd).replace("\n","").replace("\xa0","").strip()
            #   评分
            item['star'] = each.xpath(".//div[@class ='info']//div[@class ='star']/span[@class ='rating_num']/text()").extract()[0]
            #   简介
            quote = each.xpath(".//div[@class ='info']//p[@class = 'quote']/span/text()").extract()
            if len(quote) != 0:
                item['quote'] = quote[0]
            #   图片的url
            item['picture']= each.xpath(".//div[@class ='pic']//a/img/@src").extract()[0]

            # extract把xpath转换为uncido文本
        
            yield item

        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
