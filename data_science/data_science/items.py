# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataScienceItem(scrapy.Item):
    title = scrapy.Field()
    text_p = scrapy.Field() #these are the "span"
    text_all = scrapy.Field() #all the field
    text_a  = scrapy.Field() #all the links href
    pass

class Link(scrapy.Item):

    title = scrapy.Field()
    url = scrapy.Field()
