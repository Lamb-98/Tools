# _*_ coding : utf-8 _*_
# @Time : 2022/2/9 13:18
# @Author : 李洋
# @File : 84_requests_基本使用
# @Project : Python爬虫

import requests

url = 'http://www.baidu.com'

response = requests.get(url=url)

# 一个类型六个属性
# Response类型
# print(type(response))

# 设置响应的编码格式
response.encoding = 'utf-8'

# 一字符串的形式来返回网页的源码
# print(response.text)

# 返回一个url地址
# print(response.url)

# 返回的是二进制的数据
# print(response.content)

# 返回响应的状态码
print(response.status_code)

# 返回的是响应头
print(response.headers)