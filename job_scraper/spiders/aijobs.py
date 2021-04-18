import scrapy
from scrapy.loader import ItemLoader

from .base_xml_feed_spider import BaseXmlFeedSpider
from ..items import JobItem


class AiJobsSpider(BaseXmlFeedSpider):
    name = 'aijobs'
    allowed_domains = ['ai-jobs.net']
    start_urls = ['https://ai-jobs.net/sitemap.xml']
    iterator = 'iternodes'
    itertag = 'loc'

    def parse_node(self, response, node):
        return scrapy.Request(
            url=node.xpath("text()").get(),
            callback=self.get_data
        )

    def get_data(self, response):
        item = ItemLoader(response=response, item=JobItem())

        item.add_value('listing_url', response.url)
        item.add_css('job_name', 'h1::text')
        item.add_css('company', '.media-body *::text')
        item.add_css('location', 'h1 + p::text')
        item.add_css('employment_type', '.badge-secondary::text')
        item.add_css('industry', '.media-body h5::text')
        item.add_css('seniority', '.badge-info::text')
        item.add_css('date_posted', 'small:contains("Posted")::text')
        item.add_css('description', '#job-description *::text')

        return item.load_item()
