from abc import abstractmethod, ABCMeta

from scrapy.spiders import XMLFeedSpider


class BaseXmlFeedSpider(XMLFeedSpider, metaclass=ABCMeta):
    name = None
    allowed_domains = ['']
    start_urls = ['']

    @abstractmethod
    def get_data(self, response):
        pass
