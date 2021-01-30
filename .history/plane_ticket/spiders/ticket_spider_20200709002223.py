import scrapy

class TicketSpider(scrapy.Spider):
    name = "tickets"

   
        start_url =[
            "http://montreal.chineseconsulate.org/chn/zlgxw/"
        ]

    def parse(self, response):
        all = response.css('.Text_Center li').css('::text').extract()
        print(type(all))

        yield all
