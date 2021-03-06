import scrapy
import re


class TicketSpider(scrapy.Spider):
    name = "tickets"

    start_urls = [
        "http://montreal.chineseconsulate.org/chn/zlgxw/"
    ]

    def parse(self, response):
        output ={}
                
        pattern = u'\u5173\u4e8e\u516c\u5e03\u4e34\u65f6\u822a\u73ed'
        top = response.css('.Text_Center li:nth-child(1)').css('::text')[0].extract()
        
        available = re.match(pattern.encode('utf-8'), top.encode('utf-8'))
       
        output['news'] = top

        if available:
            yield output

        
        
