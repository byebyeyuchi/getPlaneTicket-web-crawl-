import scrapy
import re


class TicketSpider(scrapy.Spider):
    name = "tickets"

    start_urls = [
        "http://montreal.chineseconsulate.org/chn/zlgxw/"
    ]

    def parse(self, response):
        output ={}
                
        top = response.css('.Text_Center li:nth-child(2)').css('::text')[0].extract()
        
        available = re.search(u'\u5173\u4e8e\u516c\u5e03\u4e34\u65f6\u822a\u73ed', top.encode('utf-8'))
       
        output['news'] = top.encode('utf-8')

        if available:
            yield output

        
        
