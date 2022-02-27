# _*_ coding : utf-8 _*_
# @Time : 2022/1/12 15:07
# @Author : 李洋
# @File : 54
# @Project : Python爬虫

import urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse的类型
print(type(response))

# 按照一字节一字节去读
# content = response.read()
# print(content)

# 返回多少个字节
# content = response.read(5)
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# content = response.readlines()
# print(content)

# 返回状态码 if is 200 对了
# print(response.getcode())

# 返回url地址
# print(response.geturl())

# 获取一个状态信息
# print(response.getheaders())

