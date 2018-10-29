import scrapy
from scrapy import Selector
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from getMeMore.items import GetmemoreItem

class libgenSpider(CrawlSpider):
    name = 'libgen'
    item_count = 0
    allowed_domain = ['www.libgen.io']
    start_urls = ['http://libgen.io/search.php?req=ciencia&lg_topic=libgen&open=0&view=detailed&res=25&phrase=1&column=def']

    # rules = {
    #     # All details  (click)
    #     Rule(LinkExtractor(alow =(), restric_xpaths= ('//input[@value="detailed"]'))),
    #     # button Search  (click)
    #     Rule(LinkExtractor(alow =(), restric_xpaths= ('//input[@type="submit"]'))),
    #     # table
    #     Rule(LinkExtractor(alow =(), restric_xpaths= ('//table[@rules="cols"]'))),
    #     # title
    #     Rule(LinkExtractor(alow =(), restric_xpaths= ('//td[@colspan="2"]')),
    #                         callback = 'parse_item', follow = False),
    # }
    
    # for url in start_urls:
    #     yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item (self, response):
        ml_item = GetmemoreItem()

        # info de link
        ml_item['titulo'] = response.xpath('//td[@colspan="2"]/b/a/text()').extract()
        ml_item['autor'] = response.xpath('//td[@colspan="3"]/b/a/text()').extract()
        ml_item['img'] = response.xpath('//td[@rowspan="20"]/a/img[@width="240"]/@src').extract()
        ml_item['language'] = response.xpath('//tr[7]/td[2]/text()').extract()
        ml_item['link'] = response.xpath('//tr[11]/td[2]/a/@href').extract()
        self.item_count += 1
        if self.item_count > 5:
            raise CloseSpider('item_exceeded')
        yield ml_item

