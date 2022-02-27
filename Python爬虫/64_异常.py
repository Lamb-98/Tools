# _*_ coding : utf-8 _*_
# @Time : 2022/1/13 17:19
# @Author : 李洋
# @File : 64_异常
# @Project : Python爬虫

import urllib.request
import urllib.error

# 错网址
url = 'http://www.fdgee549481.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

try:
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
except urllib.error.HTTPError:
    print('系统正在维护...')
except urllib.error.URLError:
    print('很抱歉！系统正在维护...')
