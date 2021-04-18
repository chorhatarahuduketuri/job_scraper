import scrapy
from scrapy.loader import ItemLoader

from .base_spider import BaseSpider
from ..items import JobItem


class TheguardianSpider(BaseSpider):
    name = 'theguardian'
    allowed_domains = ['theguardian.com']
    start_urls = [
        'https://jobs.theguardian.com/searchjobs/?LocationId=1500&keywords=data+science+machine+learning&radialtown='
        'London+(Central)%2c+London+(Greater)&countrycode=GB'
    ]

    listing_css = '.button--lister-view-details::attr(href)'
    next_page_css = '.paginator__item.endpoint a::attr(href)'
    details_base_css = 'dt:contains("") + dd::text'

    def parse(self, response):
        if self.listing_css:
            listing_urls = response.css(self.listing_css).extract()
            listing_urls = [listing_url.strip() for listing_url in listing_urls]
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

    def get_data(self, response):
        item = ItemLoader(response=response, item=JobItem())

        item.add_value('listing_url', response.url)
        item.add_css('job_title', 'h1::text')
        item.add_css('company', self.details_base_css.format('Recruiter'))
        item.add_css('salary', self.details_base_css.format('Salary'))
        item.add_css('location', self.details_base_css.format('Location'))
        item.add_css('employment_type', self.details_base_css.format('Hours'))
        item.add_css('employment_type', self.details_base_css.format('Contract'))
        item.add_css('industry', self.details_base_css.format('Industry'))
        item.add_css('department', self.details_base_css.format('Job function'))
        item.add_css('seniority', self.details_base_css.format('Job level'))
        item.add_css('date_posted', self.details_base_css.format('Posted'))
        item.add_css('description', '.job-description *::text')

        yield item.load_item()
