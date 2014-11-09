# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataScienceItem(scrapy.Item):
    name = scrapy.Field()
    respons = scrapy.Field() #responsibility
    req = scrapy.Field() #requirements
    minqual = scrapy.Field() #minimum qualifications
    prefqual = scrapy.Field() #prefered qualitifications
    company = scrapy.Field() #company
    location = scrapy.Field() #location
    pass
