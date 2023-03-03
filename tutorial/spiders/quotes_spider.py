from pathlib import Path

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes" # Must be unique to project
    # Can bypass start_requests() and use start_urls
    # parse() is the default Scrapy callback
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    # Handles response downloaded foreach request.
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
