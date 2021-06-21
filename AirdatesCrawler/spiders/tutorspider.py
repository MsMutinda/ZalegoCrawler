import scrapy
from ..items import TutorcrawlerItem

class TutorSpider(scrapy.Spider):
    name = 'tutorspider'
    start_urls = [
        'https://lms.zalegoacademy.ac.ke/lms/course/index.php?categoryid=2',
        'https://lms.zalegoacademy.ac.ke/lms/course/index.php?categoryid=7',
        'https://lms.zalegoacademy.ac.ke/lms/course/index.php?categoryid=10',
        'https://lms.zalegoacademy.ac.ke/lms/course/index.php?categoryid=16',
        'https://lms.zalegoacademy.ac.ke/lms/course/index.php?categoryid=11',
        'https://lms.zalegoacademy.ac.ke/lms/course/index.php?categoryid=12',
        'https://lms.zalegoacademy.ac.ke/lms/course/index.php?categoryid=14',
        'https://lms.zalegoacademy.ac.ke/lms/course/index.php?categoryid=15',
        'https://lms.zalegoacademy.ac.ke/lms/course/index.php?categoryid=19',
    ]

    def parse(self, response):
        items = TutorcrawlerItem()
        containers = response.css('div.row div.col-lg-6 div.top_courses div.details')
        for con in containers:
            course_name = con.css('div.tc_content a h5::text').extract()
            tutor_name = con.css('div.tc_content p span.ccn_course_meta_item a::text').extract()
            yield {
                'course_name': course_name,
                'tutor': tutor_name
            }            

