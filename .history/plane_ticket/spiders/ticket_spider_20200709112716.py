import scrapy
import re


class TicketSpider(scrapy.Spider):
    name = "tickets"

    start_urls = [
        "http://montreal.chineseconsulate.org/chn/zlgxw/"
    ]

    def parse(self, response):
        output ={}
                
        pattern = '\u5173\u4e8e\u4e58\u5750\u4e34\u65f6\u822a\u73ed\u56de\u56fd'
        top = response.css('.Text_Center li:nth-child(1)').css('::text')[1].extract()
        
        available = re.search(pattern, top)
       
        output['news'] = top

        if(not available):
            yield output

        
        
