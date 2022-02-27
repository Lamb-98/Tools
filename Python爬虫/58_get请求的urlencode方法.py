# _*_ coding : utf-8 _*_
# @Time : 2022/1/12 16:29
# @Author : 李洋
# @File : 58_get请求的urlencode方法
# @Project : Python爬虫

# urlencode应用场景：多个参数的时候

import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?'
data = {
    'wd': '祢豆子',
    'sex': '女',
    'location': '日本'
}
new_data = urllib.parse.urlencode(data)
url = url + new_data

# 请求对象定制
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)

# 伪装浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获得响应内容
content = response.read().decode('utf-8')
print(content)
