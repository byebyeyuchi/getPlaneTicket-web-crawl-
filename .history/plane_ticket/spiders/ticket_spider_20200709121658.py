import scrapy
import re
from twilio.rest import Client


class TicketSpider(scrapy.Spider):
    name = "tickets"

    start_urls = [
        "http://montreal.chineseconsulate.org/chn/zlgxw/"
    ]


    def sendWhatsup(self,msg):
        TWILIO_ACCOUNT_SID="ACbf904f84a3d86d3ab355e41326f9a99f"
        TWILIO_AUTH_TOKEN="b6733f5ba23d717c129d63994eaadc72"

        client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
        from_whatsapp_number = 'whatsapp:+14155238886'
        to_whatsapp_number='whatsapp:+8615107330160'
        
        client.messages.create(from_=from_whatsapp_number, body=msg,  to=to_whatsapp_number)
    

    def parse(self, response):
        output ={}
                
        pattern = u'\u5173\u4e8e\u516c\u5e03\u4e34\u65f6\u822a\u73ed'
        top = response.css('.Text_Center li:nth-child(2)').css('::text')[0].extract()
        
        available = re.match(pattern.encode('utf-8'), top.encode('utf-8'))
       
        output['news'] = top

        if available:
            self.sendWhatsup(u'\u65b0\u822a\u73ed\u4fe1\u606f\u5df2\u516c\u5e03\u81f3\u9886\u9986\u5b98\u7f51')
            yield output

        
        
