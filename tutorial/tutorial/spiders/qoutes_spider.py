from matplotlib.pyplot import title
from pyparsing import quoted_string
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]
   
    def parse(self, response):
        quotes=response.css("div.quote")
        for quote in quotes:
            title=quote.css("span.text::text").extract_first()
            author=quote.css("small.author::text").extract_first()
            tag=quote.css("div.tags a.tag").extract()
            yield {
                "title":title,
                "author":author,
                "tag":tag
            }


