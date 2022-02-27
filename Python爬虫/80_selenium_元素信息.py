# _*_ coding : utf-8 _*_
# @Time : 2022/2/8 19:52
# @Author : 李洋
# @File : 80_selenium_元素信息
# @Project : Python爬虫

from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'
browser.get(url)

input = browser.find_element_by_id('su')
# 获取元素属性
print(input.get_attribute('class'))
# 获取标签名
print(input.tag_name)
# 获取元素文本
a = browser.find_element_by_link_text('新闻')
print(a.text)
