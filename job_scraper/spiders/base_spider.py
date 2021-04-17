from abc import abstractmethod, ABCMeta

import scrapy


class BaseSpider(scrapy.Spider, metaclass=ABCMeta):
    name = None
    allowed_domains = ['']
    start_urls = ['']

    next_page_css = ''
    listing_css = ''

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={'cookiejar': i}
            )

    def visit_next_page(self, response, css_text=''):
        if css_text:
            next_page = response.css(css_text).extract_first()
        else:
            return None
        next_page_request = None
        if next_page:
            next_page_request = scrapy.Request(
                url=response.urljoin(next_page),
                callback=self.parse,
                meta={'cookiejar': response.meta.get('cookiejar')}
            )
        return next_page_request

    def parse(self, response):
        if self.listing_css:
            listing_urls = response.css(self.listing_css).extract()
        else:
            listing_urls = []

        for listing_url in listing_urls:
            if not listing_url:
                continue
            yield scrapy.Request(
                url=response.urljoin(listing_url),
                callback=self.get_data
            )
        if self.next_page_css:
            yield self.visit_next_page(
                response=response,
                css_text=self.next_page_css
            )

    @abstractmethod
    def get_data(self, response):
        pass
