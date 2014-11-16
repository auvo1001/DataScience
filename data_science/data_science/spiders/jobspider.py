# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider
from data_science.items import DataScienceItem

class JobSpider(scrapy.Spider):
    """
    spider for the site analytictalent.com
    """
    name = "jobspider"
    allowed_domains = ["analytictalent.com"]
    start_urls = (
        'http://www.analytictalent.com/',
'http://careers.analytictalent.com/jobs/software-engineer-python-youtube-san-bruno-california-71585336-d?contextType=browse'
)
    def parse(self, response):

        items = []
        item = DataScienceItem()
        item['text_li'] =  response.xpath('//li/text()').extract() #bullet points in the texts
        item['text_span'] =  response.xpath('//span/text()').extract()
        item['text_all'] =  response.xpath('//*/text()').extract() #span class, usually all the texts
        item['title'] =  response.xpath('//title/text()').extract() #title of the page]

        items.append(item)

        filename = "software_related_job/software5.txt"
        with open(filename, 'wb') as f:
            f.write(str(items))
