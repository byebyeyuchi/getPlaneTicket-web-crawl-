import scrapy
import re


class TicketSpider(scrapy.Spider):
    name = "tickets"

    start_urls = [
        "http://montreal.chineseconsulate.org/chn/zlgxw/"
    ]

    def parse(self, response):
        output ={}
                
        pattern = '关于公布临时航班'
        top = response.css('.Text_Center li:nth-child(1)').css('::text')[1].extract()
        
        available = re.search(pattern, top)
       
        output['news'] = top

        if（available):
            yield output

        
        
