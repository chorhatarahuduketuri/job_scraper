import scrapy
from scrapy.loader import ItemLoader

from .base_spider import BaseSpider
from ..items import JobItem


class TechnojobsSpider(BaseSpider):
    name = 'technojobs'
    allowed_domains = ['technojobs.co.uk']
    start_urls = [
        'https://www.technojobs.co.uk/search.phtml/data-science-machine-learning/searchfield/locationLondon/radius5/sa'
        'lary0/sortby15'
    ]

    listing_css = '.view-job-button::attr(href)'
    details_base_css = 'th:contains("{}") + td::text'

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
        search_page_urls = response.css('.pagination a::attr(href)').extract()
        for search_page_url in search_page_urls:
            if not search_page_url:
                continue
            if search_page_url:
                yield scrapy.Request(
                    url=response.urljoin(search_page_url),
                    callback=self.parse
                )

    def get_data(self, response):
        item = ItemLoader(response=response, item=JobItem())

        item.add_value('listing_url', response.url)
        item.add_css('job_name', '.job-listing-title h1::text')
        item.add_css('company', self.details_base_css.format('Recruiter:'))
        item.add_css('salary', self.details_base_css.format('Salary/Rate:'))
        item.add_css('salary', self.details_base_css.format('Salary Notes:'))
        item.add_css('location', self.details_base_css.format('Location:'))
        item.add_css('employment_type', self.details_base_css.format('Type:'))
        item.add_css('date_posted', self.details_base_css.format('Listed on:'))
        item.add_css('start_date', self.details_base_css.format('Start Date:'))
        item.add_css('description', '.job-listing-body *::text')

        yield item.load_item()
