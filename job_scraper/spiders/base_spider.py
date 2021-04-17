import scrapy


class BaseSpider(scrapy.Spider):
    name = 'name'
    allowed_domains = ['']
    start_urls = ['']

    next_page_css = ''
    listing_css = ''

    def parse(self, response):
        pass
