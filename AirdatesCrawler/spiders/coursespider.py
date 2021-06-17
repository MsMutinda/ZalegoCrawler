import scrapy
from ..items import CoursescrawlerItem

class CourseSpider(scrapy.Spider):
    name = 'coursespider'
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
        items = CoursescrawlerItem()

        containers = response.css('div.row div.col-lg-6 div.top_courses div.details')

        for con in containers:
            title = con.css('div.tc_content a h5::text').extract()
            for sth in title:
                items['course_title'] = sth

                yield items
