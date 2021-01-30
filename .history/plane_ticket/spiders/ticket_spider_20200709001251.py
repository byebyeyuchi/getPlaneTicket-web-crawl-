import scrapy

class TicketSpider(scrapy.Spider):
    name = "tickets"

    def start_requests(self):
        urls =[
            "http://montreal.chineseconsulate.org/chn/zlgxw/"
        ]

    def parse(self, response):
        pass
