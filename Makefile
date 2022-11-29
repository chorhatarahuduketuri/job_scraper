scrapeall:
	poetry run scrapy list | poetry run xargs -I@ -n 1 scrapy crawl @ -o output/@.json

scrapeall_parallel:
	poetry run scrapy list | poetry run xargs -I@ -P 0 -n 1 scrapy crawl @ -o output/@.json