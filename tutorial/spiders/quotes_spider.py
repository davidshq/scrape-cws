from pathlib import Path

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes" # Must be unique to project
    # Can bypass start_requests() and use start_urls
    # parse() is the default Scrapy callback
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    # Handles response downloaded foreach request.
    def parse(self, response):
        # Extract data using css selectors
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        # Get the next page link, continue parsing pages
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    