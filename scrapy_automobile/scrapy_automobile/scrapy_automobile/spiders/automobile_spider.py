import scrapy
import pandas as pd
from urllib.parse import urlparse
class AutomobileSpider(scrapy.Spider):
    name = "automobile"
    articles = []
    def start_requests(self):
        urls = [
            "https://www.automobile.tn/fr/occasion"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def requestItem(self, url, response):
        yield response.follow(url, self.parse_item)


    def getData(self,response):
        for item in response.css("div.occasion-item"):
            article = {}
            url = item.css("a.details-container::attr('href')").get()
            u = "https://www.automobile.tn" + url
            article['label'] = item.css("div.thumb-caption h2 span::text").get()
            price = item.css("div.price::text").get()
            article['price'] = price.lstrip()
            article['year']  = item.css("li.year  span.value::text").get()
            article['road'] = item.css("li.road span.value::text").get()
            article['fuel'] = item.css("li.fuel span.value::text").get()
            article['boite'] = item.css("li.boite span.value::text").get()
            self.articles.append(article)
        
    def parse_item(self, response):
        article = {}
        article ['label'] = response.css("h3.page-title::text").get()
        article['price'] = response.css("div.small-price span::text").get()
        article['phone'] = response.css("button.btn-main-phone::text").get()
        all = response.css("ul.list-unstyled li span::text").getall()
        article['Kms'] = all[0]
        article['year'] = all[1]
        article['gov'] = all[2]
        article['date'] = all[3]
        self.articles.append(article)
        yield article


    def parse(self, response):
        baseUrl = "https://www.automobile.tn"
        urls = response.css("div.occasion-item a.details-container::attr('href')").getall()
        urls = [baseUrl + url for url in urls]
        for url in urls:
            yield response.follow(url, self.parse_item)
        
        next_dis = response.xpath("//li[@class = 'page-item next disabled']")
        if not next_dis:
            next = response.xpath('//li[@class="page-item next"]/a/@href').extract_first()
            nextUrl = baseUrl+next
            yield scrapy.Request(url=nextUrl)


            
