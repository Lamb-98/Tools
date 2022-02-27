# _*_ coding : utf-8 _*_
# @Time : 2022/1/13 14:32
# @Author : 李洋
# @File : 61_urllib_ajax的get请求豆瓣电影第一页
# @Project : Python爬虫

# get请求
# 获取豆瓣电影的第一页的数据 并且保存起来

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
# 数据下载到本地
# open方法默认情况下使用的是gbk的编码，if we want to save characters，那么需要再open方法中指定编码格式为utf-8
# fp = open('douban.json', 'w', encoding='utf-8')
# fp.write(content)