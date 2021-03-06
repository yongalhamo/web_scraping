# -*- coding: utf-8 -*-
import scrapy


class GlassshopSpiderSpider(scrapy.Spider):
    name = 'glassShop_spider'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['http://www.glassesshop.com/bestsellers/']


    def start_request(self):
        yield scrapy.Request(url='http://www.glassesshop.com/bestsellers/',
                             callback=self.parse, headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
            })



    def parse(self, response):
        for product in response.xpath("//div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']"):
            yield{
                'Product name': product.xpath(".//div[@class='p-title']/a/@title").get(),
                'product url' :  response.urljoin(product.xpath(".//div[@class='p-title']/a/@href").get()),
                'product image link':product.xpath(".//div[@class='product-img-outer']/a/img[2]/@data-src").get(),
                'product price': product.xpath(".//div[@class='p-price']/div/span/text()").get()
            }

        next_page = response.xpath("//a[@class='page-link']/@href").get()

        if next_page:
            yield scrapy.Request(url= next_page, callback=self.parse, headers = {
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
            })
