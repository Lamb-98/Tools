# _*_ coding : utf-8 _*_
# @Time : 2022/2/8 17:17
# @Author : 李洋
# @File : 76_解析_bs4爬取星巴克数据
# @Project : Python爬虫

import urllib.request

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

# //ul[@class="grid padded-3 product"]/li/a/strong/text()
name_list = soup.select('ul[class="grid padded-3 product"] strong')
pic_list = soup.select('div[class="preview circle"]')
for pic in pic_list:
    print(pic.attrs.get('style'))


# print(name_list)
#
# for name in name_list:
#     print(name.get_text())