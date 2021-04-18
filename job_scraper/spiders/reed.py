from scrapy.loader import ItemLoader

from .base_spider import BaseSpider
from ..items import JobItem


class ReedSpider(BaseSpider):
    name = 'reed'
    allowed_domains = ['reed.co.uk']
    start_urls = [
        'https://www.reed.co.uk/jobs/data-science-machine-learning-jobs-in-london?sortby=DisplayDate&proximity=3'
    ]

    listing_css = '.gtmJobTitleClickResponsive::attr(href)'
    next_page_css = '#nextPage::attr(href)'
    details_base_css = 'span[itemprop="{}"] *::text'

    def get_data(self, response):
        item = ItemLoader(response=response, item=JobItem())

        item.add_value('listing_url', response.url)
        item.add_css('job_title', 'h1::text')
        item.add_css('company', self.details_base_css.format('name'))
        item.add_css('salary', self.details_base_css.format('baseSalary'))
        item.add_css('location', self.details_base_css.format('address'))
        item.add_css('requirements', 'span[itemprop="description"] > p > strong::text')
        item.add_css('employment_type', self.details_base_css.format('employmentType'))
        item.add_css('date_posted', self.details_base_css.format('hiringOrganization'))
        item.add_css('description', self.details_base_css.format('description'))

        yield item.load_item()
