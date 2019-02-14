# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from scrapy_redis.spiders import RedisSpider
from selenium import webdriver
from sfnews.utils.InsertRedis import inserintota
from selenium.webdriver.support.ui import WebDriverWait


class FnewsSpider(Spider):
    name = 'fnews'
    allowed_domains = ['finance.sina.com.cn/china/']
    start_urls = ['http://finance.sina.com.cn/china//']
    news_cnt = 5
    next_xpath= "//span[@class='pagebox_next']/a"

    def __init__(self):
        super(FnewsSpider, self).__init__()
        self.chrome_options = webdriver.ChromeOptions()  # 获取ChromeWebdriver配置文件
        prefs = {"profile.managed_default_content_settings.images": 2}  # 设置不加载图片以加快速度
        self.chrome_options.add_experimental_option("prefs", prefs)
        self.chrome_options.add_argument("--headless")  # 不使用GUI界面
        self.chrome_options.add_argument("--disable-gpu")  # 禁用GPU渲染加速
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)  # 创建ChromeWebdriver
        self.driver.set_page_load_timeout(10)  # 设置连接超时时间为15s


    def parse(self, response):
        self.driver.get(response.url)
        for i in range(self.news_cnt):
            wait = WebDriverWait(self.driver, 2)
            wait.until(
                lambda driver: driver.find_element_by_xpath('//*[@id="feedCardContent"]/div[1]/div/h2/a'))  # 内容加载完成后爬取
            sel_list = self.driver.find_elements_by_xpath('//*[@id="feedCardContent"]/div[1]/div/h2/a')
            for sel in sel_list:
                inserintota(sel.get_attribute("href"))
            wait = WebDriverWait(self.driver, 2)
            wait.until(
                lambda driver: driver.find_element_by_xpath(self.next_xpath))  # 内容加载完成后爬取
            next_page = self.driver.find_element_by_xpath(self.next_xpath)
            next_page.click()







