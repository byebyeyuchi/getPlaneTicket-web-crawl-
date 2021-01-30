import scrapy


class TicketSpider(scrapy.Spider):
    name = "tickets"

    start_urls = [
        "http://montreal.chineseconsulate.org/chn/zlgxw/"
    ]

    def parse(self, response):
        output ={}
        all = response.css('.Text_Center li').css('::text').extract()
        top = response.css('.Text_Center li:nth-child(1)').css('::text')[0].extract()
        
        for word in all:
            print()
        
        output['news'] = top
        yield output
