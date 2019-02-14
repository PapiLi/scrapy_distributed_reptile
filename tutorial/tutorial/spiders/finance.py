# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from scrapy_redis.spiders import RedisSpider

class FinanceSpider(RedisSpider):
    # 继承自RedisSpider，则start_urls可以从redis读取
    # 继承自BaseSpider，则start_urls需要写出来
    name = 'finance'
    redis_key = 'content_urls'

    def parse(self, response):
        item= TutorialItem()
        title=response.selector.xpath("/html/head/meta[@property='og:title']/@content").extract_first()
        time = response.selector.xpath("/html/head/meta[@property='article:published_time']/@content").extract_first()
        author =response.selector.xpath("/html/head/meta[@property='article:author']/@content").extract_first()
        url =response.selector.xpath("/html/head/meta[@property='og:url']/@content").extract_first()
        articles =response.css("#artibody p::text").extract()
        content=''
        for article in articles:
            if article.isspace():
                continue
            content += article.lstrip()
        item["title"]=title
        item["time"]=time
        item["author"] =author
        item["url"] =url
        item["content"] =content
        yield item
