import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from data_science.items import DataScienceItem
from scrapy.contrib import linkextractors
#def get_category():
#    #first, get all the anchor tags
#    scrapy.fetch("http://www.analytictalent.com/")
#    anchor = response.xpath('//a/@href').extract()
#    #then, extract all category out
#    category  = [s.replace("http://careers.analytictalent.com/jobs/browse/category/","") for s in anchor if "category" in s]
#    top = "http://careers.analytictalent.com/jobs/search/results?category%5B0%5D="
#    bot = "&format=rss"
#    url = []
#    for cat in category:
#        url.append(top+cat+url)
#
#    return url
#    #

class SiteSpider(scrapy.Spider):
    """
    spider for the site analytictalent.com
    """
    name = "sitespider"
    allowed_domains = ["analytictalent.com"]
    start_urls = (
        'http://www.analytictalent.com/',
        )
    rules = (Rule(linkextractors.lxmlhtml.LxmlLinkExtractor(allow=("category" ),)
    , callback="parse_items", follow= True),
    )
    def parse(self, response):

        items = []
        item = DataScienceItem()
        item['title'] =  response.xpath('//title/text()').extract() #title of the page
        item['text_span'] =  response.xpath('//span/text()').extract() #span class, usually all the texts
        item['text_li'] =  response.xpath('//li/text()').extract() #bullet points in the texts
        items.append(item)

        filename = "sitecrawl.txt"
        with open(filename, 'wb') as f:
            f.write(str(items))
