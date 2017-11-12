from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.wikiSpider import items


class ArticleSpider(Spider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia/wiki/Main-Page",
                  "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]

    def parse(self, response):
        item = items.Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: "+title)
        item['title'] = title
        return item