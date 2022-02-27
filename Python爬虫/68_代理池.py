# _*_ coding : utf-8 _*_
# @Time : 2022/1/14 15:29
# @Author : 李洋
# @File : 68_代理池
# @Project : Python爬虫

import urllib.request
# 代理池，用列表来装，里头是字典
proxies_pool = [
    {'http:': '45.77.126.194:443'},
    {'http:': '45.77.126.194:443'},
]

import random
# 随机从代理池中抽一个出来
proxies = random.choice(proxies_pool)

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
