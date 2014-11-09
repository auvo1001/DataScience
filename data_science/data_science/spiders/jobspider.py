# -*- coding: utf-8 -*-
import scrapy
from data_science.items import DataScienceItem

class JobSpider(scrapy.Spider):
    """
    spider for the site analytictalent.com
    """
    name = "jobspider"
    allowed_domains = ["analytictalent.com"]
    start_urls = (
        'http://www.analytictalent.com/',
        'http://careers.analytictalent.com/jobs/lead-quantitative-analyst-operations-decision-support-google-mountain-view-california-69333430-d?contextType=browse',
    )

    #rules = (Rule(SgmlLinkExtractor(allow=("jobs", ),)
    #, callback="parse_items", follow= True),
    #)

    def parse(self, response):
        items = []  #name, respons, req, minqual , prefqual, company, location

        for sel in response.xpath('//*'):
            item = DataScienceItem()
            item['name'] = sel.xpath('text()').extract()
            items.append(item)

        filename = "datascience.txt"
        with open(filename, 'wb') as f:
            f.write(str(items))
