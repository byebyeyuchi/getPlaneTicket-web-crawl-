import scrapy


class TicketSpider(scrapy.Spider):
    name = "tickets"

    start_urls = [
        "http://montreal.chineseconsulate.org/chn/zlgxw/"
    ]

    def parse(self, response):
        output ={}
        re = '\u5173\u4e8e\u4e58\u5750\u4e34\u65f6\u822a\u73ed\u56de\u56fd'
        top = response.css('.Text_Center li:nth-child(1)').css('::text')[0].extract()
        
        
        stock_online = not re.search("Sold out", ''.join(online))
        output['news'] = top
        yield output
