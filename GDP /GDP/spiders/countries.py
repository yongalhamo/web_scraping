# -*- coding: utf-8 -*-
import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['http://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        ratio = response.xpath(".//td[2]/text()").get()
        for country in countries:
            name = country.xpath(".//text()").get()

            yield{
                'Country_name': name,
                'gdp_ratio':ratio
            }


    #         link = country.xpath(".//@href").get()
    #
    #         yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})
    #         #yield response.follow(url=link, callback=self.parse_country, meta={'National Debt to GDP Ratio': ratio})
    #
    #
    #
    # def parse_country(self,response):
    #     name = response.request.meta['country_name']
    #     #ratio = response.request.meta['National Debt to GDP Ratio']
    #     rows = response.xpath("((//table[@class='jsx-1487038798 table table-striped tp-table-body'])[2])[1]/tbody/tr")
    #     for row in rows:
    #         year = row.xpath(".//td[1]/text()").get()
    #         #growth = row.xpath(".//td[3]").get()
    #
    #         yield{
    #             'country_name': name,
    #             #'National Debt to GDP Ratio': ratio,
    #             'year': year
    #             #'Population_Growth_Rate': growth
    #
    #         }

