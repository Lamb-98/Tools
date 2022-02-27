# _*_ coding : utf-8 _*_
# @Time : 2022/1/14 13:17
# @Author : 李洋
# @File : 66_handler处理器的基本使用
# @Project : Python爬虫
import urllib.request

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# （1）获取handler对象
handler = urllib.request.HTTPHandler()

# （2）获取opener对象
opener = urllib.request.build_opener(handler)

# （3）调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)