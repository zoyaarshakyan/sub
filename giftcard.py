# -*- coding: utf-8 -*-
import scrapy


class GiftcardSpider(scrapy.Spider):
    name = 'giftcard'
    allowed_domains = ['https://www.giftcardmall.am/en']
    start_urls = []
    i=1
    while i<3:
        URL = 'https://www.giftcardmall.am/en/?page=' + str(i)
        start_urls.append(URL)
        i+=1
    def parse(self, response):
         filename = "giftcardmall"+response.url[-1]+".html"
        with open(filename,'w') as f:
            f.write(response.body)

    def parse(self, response):
    	for g in response.css('div.col-md-10 col-md-offset-0 col-xs-12 padding-left-0').extract_first():
            yield {"company_name": g.css('h4.card_title:: text'),
            "price": g.css('p.card_sum:: text').re('[0-9]+'),
            