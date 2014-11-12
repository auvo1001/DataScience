# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from data_science.items import DataScienceItem
from data_science.spiders import methods

class JobSpider(scrapy.Spider):
    """
    spider for the site analytictalent.com
    """
    name = "jobspider"
    allowed_domains = ["analytictalent.com"]
    start_urls = (
        #'http://www.analytictalent.com/',
        'http://careers.analytictalent.com/jobs/lead-quantitative-analyst-operations-decision-support-google-mountain-view-california-69333430-d?contextType=browse'
        #hard code this link for testing. However, each individual job can run using this spider,
    )

    #rules = (Rule(SgmlLinkExtractor(allow=("jobs", ),)
    #, callback="parse_items", follow= True),
    #)
    print methods.get_category()
    def parse(self, response):

        items = []


        item = DataScienceItem()
        item['title'] =  response.xpath('//title/text()').extract() #title of the page
        item['text_span'] =  response.xpath('//span/text()').extract() #span class, usually all the texts
        item['text_li'] =  response.xpath('//li/text()').extract() #bullet points in the texts
        items.append(item)


        filename = "datascience.txt"
        with open(filename, 'wb') as f:
            f.write(str(items))


class SiteSpider(scrapy.Spider):
    """
    spider for the site analytictalent.com
    """
    name = "jobspider"
    allowed_domains = ["analytictalent.com"]
    start_urls = (
        'http://www.analytictalent.com/',
        )

    #rules = (Rule(SgmlLinkExtractor(allow=("jobs", ),)
    #, callback="parse_items", follow= True),
    #)
