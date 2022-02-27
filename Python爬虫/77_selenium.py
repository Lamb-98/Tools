# _*_ coding : utf-8 _*_
# @Time : 2022/2/8 18:21
# @Author : 李洋
# @File : 77_selenium
# @Project : Python爬虫

from selenium import webdriver

# 创建浏览器操作对象
path = 'chromedriver.exe'

browser = webdriver.Chrome(path)

# 访问网站
url = 'https://www.baidu.com'

browser.get(url)

# # 新方法，没有警告
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# s = Service('chromedriver.exe')
# driver = webdriver.Chrome(service=s)
#
# driver.get('https://www.baidu.com/')
# driver.quit()
