# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class JobScraperPipeline:
    def process_item(self, item, spider):
        # TODO: better item processing
        print(f'item: {item}')
        for k, v in item.items():
            item[k] = ' '.join([string.strip().replace('  ', ' ') for string in v if string.strip()]) \
                .replace('  ', ' ') \
                .replace(r'\xa0', ' ').replace(r'\n', ' ').replace(r'\r', ' ').replace(r'\t', ' ') \
                .replace('  ', ' ') \
                .strip()
        return item
