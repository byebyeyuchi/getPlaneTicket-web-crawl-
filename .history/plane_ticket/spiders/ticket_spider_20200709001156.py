import scrapy

class TicketSpider(scrapy.Spider):
    name = "tickets"

    def parse(self, response)