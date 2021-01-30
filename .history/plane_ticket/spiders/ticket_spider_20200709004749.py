import scrapy


class TicketSpider(scrapy.Spider):
    name = "tickets"

    start_urls = [
        "http://montreal.chineseconsulate.org/chn/zlgxw/"
    ]

    def parse(self, response):
        output ={}
        top = response.css('.Text_Center li:nth-child(1)').css('::text')[0].extract()
        if top
        
        for word in all:
            print(word)

        output['news'] = top
        yield output
