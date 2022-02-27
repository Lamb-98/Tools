# _*_ coding : utf-8 _*_
# @Time : 2022/1/12 16:05
# @Author : 李洋
# @File : 57_get请求的quote方法
# @Project : Python爬虫

import urllib.request
import urllib.parse

# 将中文编码为Unicode
name = urllib.parse.quote('祢豆子')
url = 'https://www.baidu.com/s?wd=' + name

# 定制headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应内容
content = response.read().decode('utf-8')

print(content)