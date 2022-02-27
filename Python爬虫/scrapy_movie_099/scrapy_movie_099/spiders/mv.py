import scrapy
from scrapy_movie_099.items import ScrapyMovie099Item

class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        # 要第一页的名字，第二页的图片
        a_list = response.xpath('//ul//table//a[2]')

        for a in a_list:
            # 获取第一页的名字和第二页的地址
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            # 第二页的地址是
            url = 'https://www.ygdy8.net' + href

            # 对第二页的链接发起访问,注意修改allowed_domains
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})

    def parse_second(self, response):
        # 注意如果拿不到数据的情况下一定检查你的xpath语法是否正确
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        # 接受到请求的那个meta参数的值
        name = response.meta['name']

        moive = ScrapyMovie099Item(src=src, name=name)

        yield moive
