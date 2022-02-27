import scrapy
# 导入类，虽然报错但不影响
from scrapy_dangdang_095.items import ScrapyDangdang095Item


class DangSpider(scrapy.Spider):
    name = 'dang'
    # 如果是多页下载的话，那么必须调整allowed_domains的范围，一般情况下只写域名
    allowed_domains = ['category.dangdang.com']
    # 注意删除.html后面的/
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']

    base_url = 'http://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        # pipelines 下载数据
        # items 定义数据结构
        # src = //ul[@id="component_59"]//li//img/@src
        # alt = //ul[@id="component_59"]//li//img/@alt
        # price = //ul[@id="component_59"]//li//p[@class="price"]/span[1]
        # 所有的selector对象都可以再次调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]//li')

        for li in li_list:

            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()

            # 第一张图片没有data-original，跟后面的不一样
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()

            book = ScrapyDangdang095Item(src=src, name=name, price=price)

            # 获取一个book就将book交给pipelines
            yield book

        # 每一页的爬取的业务逻辑全都是一样的，所以我们只需要执行的那个页的请求再次调用parse方法
        # 第一页：http://category.dangdang.com/cp01.01.02.00.00.00.html
        # 第二页：http://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
        # 第三页：http://category.dangdang.com/pg3-cp01.01.02.00.00.00.html

        if self.page < 100:
            self.page = self.page + 1

            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'

            # 怎么调用parse方法
            # scrapy.Request就是scrapy的get请求
            # url就是请求地址
            # callback就是你要执行的那个函数，不需要加()
            yield scrapy.Request(url=url, callback=self.parse)
