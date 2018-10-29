# import scrapy
    
# class libgenSpider(scrapy.Spider):
#     name = 'libgen'
#     item_count = 0
#     allowed_domains = ['http://libgen.io']

#     rules = {
#         Rule(LinkExtractor{alow ={}, restric_xpaths= '//table[@rules="cols"]'})
#     }
    
#     def start_requests(self):
#         urls = [
#             'http://libgen.io/search.php?req=ciencia&lg_topic=libgen&open=0&view=detailed&res=25&phrase=1&column=def',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#     def parse(self, response):
#         filename = 'libgen.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)
#         pass