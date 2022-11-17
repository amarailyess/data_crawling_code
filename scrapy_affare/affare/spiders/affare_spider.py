import scrapy


class AffareSpiderSpider(scrapy.Spider):
    name = 'affare_spider'
    page_index = 1
    allowed_domains = ['www.affare.tn']
    start_urls = ['https://www.affare.tn/petites-annonces/tunisie/voiture-neuve-occassion-prix-tayara-a-vendre?o=']

    def start_requests(self):
        for url in self.start_urls:
            u = url + str(self.page_index)
            yield scrapy.Request(url=u, callback=self.parse)

    def parse(self, response):
        ads = response.xpath("//div[@class='AnnoncesList_product_x__BzrCL   ']")
        for ad in ads:
            d = {}
            d['title'] = ad.xpath(".//div[@class='AnnoncesList_item_title__cee2m']/text()").extract_first()
            d['price'] = ad.xpath(".//span[@class='AnnoncesList_price__J_vIo']/text()").extract_first()
            d['place'] = ad.xpath(".//p[@class='one-line']/text()").extract_first()
            p = ad.xpath(".//p[@class='AnnoncesList_params_st__2fGEu one-line']")
            det = p.xpath(".//span/text()").getall()
            if len(det)<2:
                d['fuel']  = det[0]
            if len(det)>=2 and len(det)<3:
                d['year']  = det[1]
            if len(det) >= 3:
                d['kms']   = det[2]
            
            yield d

        if self.page_index < 5:
            self.page_index += 1
            next_url = self.start_urls[0] + str(self.page_index)
            yield scrapy.Request(url= next_url, callback=self.parse)