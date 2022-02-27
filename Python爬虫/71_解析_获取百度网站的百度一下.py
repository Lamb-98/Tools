# _*_ coding : utf-8 _*_
# @Time : 2022/1/15 12:42
# @Author : 李洋
# @File : 71_解析_获取百度网站的百度一下
# @Project : Python爬虫

import urllib.request

url = 'https://baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 解析网页源码，来获取我们想要的数据
from lxml import etree

# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据 xpath的返回值是一个列表类型的数据
result = tree.xpath('//input[@id="su"]/@value')[0]

print(result)