# _*_ coding : utf-8 _*_
# @Time : 2022/1/12 15:41
# @Author : 李洋
# @File : 56_请求对象的定制
# @Project : Python爬虫

import urllib.request
url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

# 因为urlopen方法中不能存储字典 所以headers不能直接传进去
# 请求对象的定制
# 注意 因为参数顺序的问题  不能直接写url 和 headers 中间还有一个data参数，要用关键字传参
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)