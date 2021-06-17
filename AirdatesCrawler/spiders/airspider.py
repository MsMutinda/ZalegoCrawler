import scrapy
from ..items import AirdatescrawlerItem

class AirdateSpider(scrapy.Spider):
    name = 'airdatespider'
    start_urls = [
        'https://lms.zalegoacademy.ac.ke/lms/course/index.php'
    ]

    def parse(self, response):
        items = AirdatescrawlerItem()

        containers = response.css('div.row div.col-lg-6 div.top_courses div.details')

        for con in containers:
            title = con.css('div.tc_content h5 a::text').extract()
            for sth in title:
                items['title'] = sth

                yield items
