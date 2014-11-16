# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataScienceItem(scrapy.Item):
    title = scrapy.Field()
    text_span = scrapy.Field() #these are the "span"
    text_li = scrapy.Field() #these are the bullet points
    text_all = scrapy.Field()

    pass
