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
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')
