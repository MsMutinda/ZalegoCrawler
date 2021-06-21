# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CategorycrawlerItem(scrapy.Item):
    title = scrapy.Field()

class CoursescrawlerItem(scrapy.Item):
    course_title = scrapy.Field()

class TutorcrawlerItem(scrapy.Item):
    tutor = scrapy.Field()