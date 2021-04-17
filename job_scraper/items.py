# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
    location = scrapy.Field()
    requirements = scrapy.Field()
    employment_type = scrapy.Field()
    industry = scrapy.Field()
    department = scrapy.Field()
    seniority = scrapy.Field()
    date_posted = scrapy.Field()
    description = scrapy.Field()
    pass
