from scrapy.loader import ItemLoader

from .base_spider import BaseSpider
from ..items import JobItem


class IndeedSpider(BaseSpider):
    name = 'indeed'
    allowed_domains = ['indeed.com']
    start_urls = ['https://uk.indeed.com/jobs?q=Data+Science+Machine+Learning&l=London&radius=5&sort=date']

    listing_css = 'a.jobtitle::attr(href)'
    next_page_css = 'a[aria-label="Next"]::attr(href)'

    def get_data(self, response):
        item = ItemLoader(response=response, item=JobItem())

        item.add_value('listing_url', response.url)
        item.add_css('job_title', 'h1::text')
        item.add_css('company', '.jobsearch-InlineCompanyRating .icl-u-lg-mr--sm::text')
        item.add_css('location', '.jobsearch-JobInforHeader-subtitle *::text')
        item.add_css('employment_type', 'span.jobsearch-JobMetadataHeader-item::text')
        item.add_css('industry', '.jobsearch-CompanyAvatar-description *::text')
        item.add_css('date_posted', '.jobsearch-JobMetadataFooter *::text')
        item.add_css('description', '#jobDescriptionText *::text')

        yield item.load_item()
