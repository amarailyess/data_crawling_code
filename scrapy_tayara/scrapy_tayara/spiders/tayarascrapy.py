import scrapy
import pandas as pd
class TayarascrapySpider(scrapy.Spider):
    i = 1
    name = 'tayarascrapy'
    allowed_domains = ['www.tayara.tn']
    start_urls = ['https://www.tayara.tn/fr/search/?category=V%C3%A9hicules&page=']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url+str(self.i), callback=self.parse)

    def requestItem(self, url, response):
        yield response.follow(url, self.parse2)

    def parse2(self, response):
        data = {}
        data['title'] = response.xpath("//h1[@class='text-gray-700 font-bold text-2xl font-arabic']/text()").extract_first()
        data['price'] = response.xpath("//data[@class='text-red-600 font-bold font-arabic  text-2xl']/@value").extract_first()
        data['kms'] = response.xpath("//span[@class='flex flex-col']//span[@class='text-gray-700 text-xs font-medium']/text()").extract_first()
        data['tel'] = response.xpath("//a[@class='lg:hidden']/@href").extract_first()[8:]
        data['place'] = response.xpath("//div[@class='flex items-center space-x-1 mb-1']//span/text()").extract_first().split(',')[0][:-1]
        yield data        

    def parse(self, response):
        ads = response.xpath("//article[@class='mx-auto']//a/@href")
        for ad in ads:
            yield response.follow(url=ad, callback=self.parse2)
            
        self.i += 1
        if self.i <10:
            url_ = response.urljoin(self.start_urls[0]+str(self.i))
            yield scrapy.Request(url=url_, callback=self.parse)
        
        

    
        
