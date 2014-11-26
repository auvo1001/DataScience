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
        'http://careers.analytictalent.com/jobs/advanced-technologist-level-3-4-huntsville-alabama-72055208-d?contextType=rss',
         'http://careers.analytictalent.com/jobs/aerospace-systems-modeling-and-simulation-engineer-level-2-3-huntsville-alabama-72055209-d?contextType=rss',
         'http://careers.analytictalent.com/jobs/parallel-database-systems-engineer-level-2-3-huntsville-alabama-72060146-d?contextType=rss',
)
    def parse(self, response):

        ###urlFile has to change per the local path
        for site in response:
            count +=1
            items = []
            item = DataScienceItem()
            item['text_a'] =  response.xpath('//a/@href').extract() #bullet points in the texts
            item['text_all'] =  response.xpath('//*/text()').extract() #span class, usually all the texts
            item['title'] =  response.xpath('//title/text()').extract() #title of the page]
            item['text_p'] =  response.xpath('//p/text(x)').extract() #span class, usually all the texts

            filename = "ttt"
            with open(filename+str(count)+".txt", 'wb') as f:
                f.write(str(items))
