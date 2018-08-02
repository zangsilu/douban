from scrapy import cmdline

cmdline.execute('scrapy crawl douban -o data.json'.split())


