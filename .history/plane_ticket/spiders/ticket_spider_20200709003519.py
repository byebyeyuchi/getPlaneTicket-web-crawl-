import scrapy


class TicketSpider(scrapy.Spider):
    name = "tickets"

    start_urls = [
        "http://montreal.chineseconsulate.org/chn/zlgxw/"
    ]

    def parse(self, response):
        all = response.css('.Text_Center li').css('::text').extract()
        top = response.css('.Text_Center li:nth-child(1)')
        print(type(all))

        yield response.css('.Text_Center li').css('::text')[0].extract()
