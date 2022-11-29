To run all spiders in series: `scrapy list | xargs -n 1 scrapy crawl`
To run all spiders in parallel: `scrapy list | xargs -P 0 -n 1 scrapy crawl`
To run all spiders and record their results: `scrapy list | xargs -I@ -n 1 scrapy crawl @ -o output/@.json`
To run all spiders and record their results: `scrapy list | xargs -I@ -P 0 -n 1 scrapy crawl @ -o output/@.json`