# _*_ coding : utf-8 _*_
# @Time : 2022/2/9 13:29
# @Author : 李洋
# @File : 85_requests_get请求
# @Project : Python爬虫

import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

data = {
    'wd': '北京'
}

# params 参数
# kwargs 字典
response = requests.get(url=url, params=data, headers=headers)

content = response.text

print(content)

# 参数使用params传递
# 参数无需urlencode编码
# 不需要请求对象的定制
# url中的?可加可不加
