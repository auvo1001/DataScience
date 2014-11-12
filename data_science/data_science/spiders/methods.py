import scrapy

def get_category():
    #first, get all the anchor tags
    scrapy.fetch("http://www.analytictalent.com/")
    anchor = response.xpath('//a/@href').extract()
    #then, extract all category out
    category  = [s.replace("http://careers.analytictalent.com/jobs/browse/category/","") for s in anchor if "category" in s]
    top = "http://careers.analytictalent.com/jobs/search/results?category%5B0%5D="
    bot = "&format=rss"
    url = []
    for cat in category:
        url.append(top+cat+url)

    return url
    #
