import scrapy

class TicketSpider(scrapy.Spider):
    name = "tickets"

    def start_requests(self):
        urls =[]

    def parse(self, response):
