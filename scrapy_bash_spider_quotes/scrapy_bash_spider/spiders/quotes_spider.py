import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_bash_spider'
    
    start_urls = ['file:///home/databiz33/data_crawling/scrapy_bash_spider_quotes/output.html']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse2)

    def parse1(self, response):
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            yield {'text':text, 'author':author, 'tags':tags}
    
    def parse2(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            text = quote.xpath(
                ".//span[@class = 'text']/text()"
            ).extract_first()
            author = quote.xpath(
                ".//small[@class = 'author']/text()"
                ).extract_first()
            tags_node = quote.xpath(".//div[@class = 'tags']")
            tags = tags_node.xpath(".//a[@class = 'tag']/text()").getall()
            yield {'text': text, 'author': author, 'tags':tags}
            
        next_page = response.xpath(
            "//li[@class='next']//a/@href"
            ).extract_first()
