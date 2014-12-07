import scrapy
from data_science.items import Link


class rssSpider(scrapy.Spider):
    """
    spider for the site analytictalent.com RSS

    """
    name = "rssspider"
    allowed_domains = ["http://www.analytictalent.com/"]
    start_urls = (
        'http://careers.analytictalent.com/jobs/search/results?rows=50&category%5B0%5D=math&format=rss',
        )

    def parse(self, response):

        items = []
        item = Link()
        item['title'] = response.xpath('//title/text()').extract()
        item['url'] = response.xpath('//link/text()').extract()

        items.append(item)

        filename = "listURL.txt"
        with open(filename, 'wb') as f:
            f.write(str(items))
