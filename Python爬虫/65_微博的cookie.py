# _*_ coding : utf-8 _*_
# @Time : 2022/1/13 17:40
# @Author : 李洋
# @File : 65_微博的cookie
# @Project : Python爬虫

import urllib.request

url = 'https://weibo.cn/6693875709/info'

headers = {
    # ':authority': 'weibo.cn',
    # ':method': 'GET',
    # ':path': '/6693875709/info',
    # ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # cookie是关键
    'cookie': '_T_WM=b8b3b85638a9f64f8035fa7c5a4cdbb0; SUB=_2A25M24P5DeRhGeBI4lEZ9yvLyzWIHXVsJy2xrDV6PUJbktAKLVXzkW1NRnz6OiF6jXHey6JFWSlEdk2jSHkNS5bN; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5um1hkFMJGK_Tqia8hYNX55NHD95QcSo.01hMfS054Ws4DqcjMi--4i-zRi-8Fi--fi-z7iKysi--ciKLsi-27q7tt; SSOLoginState=1642066857',
    # referer 判断当前路径是不是由上一个路径进来的，一般情况下是做图片防盗链
    'referer': 'https://weibo.cn/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
