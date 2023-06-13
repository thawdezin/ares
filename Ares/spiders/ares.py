import scrapy
import asyncio
import aiohttp
import random

class AresSpider(scrapy.Spider):
    name = 'ares'
    allowed_domains = ['thawdezin.netlify.app']
    start_urls = ['https://thawdezin.netlify.app/']

    def parse(self, response):
        # Extract data from the current page
        # Replace the code below with your own logic to extract the desired data
        title = response.css('title::text').get()
        body = response.css('body::text').get()

        # Process the extracted data as needed (e.g., store in a database, save to a file, etc.)
        # Replace the code below with your own logic
        print(f'Title: {title}')
        print(f'Body: {body}')

        # Follow links to other pages on the website
        # Replace the code below with the appropriate selectors and logic for your target website
        for link in response.css('a::attr(href)').getall():
            yield response.follow(link, callback=self.parse, errback=self.handle_error)

    def handle_error(self, failure):
        # Print the error and skip to the next URL
        self.logger.error(repr(failure))
