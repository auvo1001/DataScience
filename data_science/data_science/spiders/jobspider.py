# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from data_science.items import DataScienceItem

class JobSpider(scrapy.Spider):
    """
    spider for the site analytictalent.com
    """
    name = "jobspider"
    allowed_domains = ["analytictalent.com"]
    #urlFile = "C:\\Users\\a\\Google Drive\\workspace\\DataScience\\data_science\\listURL.txt"
    #urlread = open(urlFile,'rb')
    #urlFile.close() not necessary
    #filedict = urlread.read()
    count = 0
    start_urls = (
         'http://careers.analytictalent.com/jobs/data-scientist-machine-learning-expert-redwood-city-california-94065-72182506-d?contextType=rss',
         'http://careers.analytictalent.com/jobs/the-channel-4-data-planning-analytics-phd-scholarship-2015-london-england-72171435-d?contextType=rss',
    )
    def parse(self, response):

        ###urlFile has to change per the local path

        items = []
        item = DataScienceItem()
        item['text_a'] =  response.xpath('//a/@href').extract() #bullet points in the texts
        item['text_all'] =  response.xpath('//*/text()').extract() #span class, usually all the texts
        item['title'] =  response.xpath('//title/text()').extract() #title of the page]
        item['text_p'] =  response.xpath('//p/text()').extract() #span class, usually all the texts

        items.append(item)

        filename = "test.txt"
        with open(filename, 'wb') as f:
            f.write(str(items))
