import scrapy

class TicketSpider(scrapy.Spider):
    name = "tickets"

    def start_requests(self){}

    def parse(self, response):
