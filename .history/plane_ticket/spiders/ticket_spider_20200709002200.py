import scrapy

class TicketSpider(scrapy.Spider):
    name = "tickets"

    def start_request(self):
        url =[
            "http://montreal.chineseconsulate.org/chn/zlgxw/"
        ]

    def parse(self, response):
        all = response.css('.Text_Center li').css('::text').extract()
        print(type(all))

        yield all
