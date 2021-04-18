# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    listing_url = scrapy.Field()
    job_title = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
    location = scrapy.Field()
    requirements = scrapy.Field()
    employment_type = scrapy.Field()
    industry = scrapy.Field()
    department = scrapy.Field()
    seniority = scrapy.Field()
    date_posted = scrapy.Field()
    start_date = scrapy.Field()
    description = scrapy.Field()
    pass
