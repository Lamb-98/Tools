# _*_ coding : utf-8 _*_
# @Time : 2022/1/12 14:53
# @Author : 李洋
# @File : 53
# @Project : Python爬虫

# 使用urllib来获取百度首页的源码
import urllib.request

# 定义url
url = 'http://www.baidu.com/'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 获取响应中的页面的源码
# read 方法  返回的是字节形式的二进制数据
# 将二进制数据转化为字符串
# 二进制->字符串：解码  decode('编码的格式')
content = response.read().decode('utf-8')

# 打印
print(content)