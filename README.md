# scrapy_distributed_reptile
scrapy写的爬取新浪财经新闻的分布式爬虫
-sfnews是主爬虫，爬取新浪财经新闻的链接存储到redis数据库中。我是放在阿里云上的。
-tutprial是从爬虫，从主机的redis端口请求新闻链接，然后爬取新闻内容存储在mongdb数据库。
