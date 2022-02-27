# _*_ coding : utf-8 _*_
# @Time : 2022/2/8 20:22
# @Author : 李洋
# @File : 81_selenium_交互
# @Project : Python爬虫
from selenium import webdriver

# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'
browser.get(url)

import time
time.sleep(1)

# 获取文本框的对象
input = browser.find_element_by_id('kw')

# 在文本框中输入周杰伦
input.send_keys('Nezuko')

time.sleep(2)

# 获取百度一下的按钮
button = browser.find_element_by_id('su')

# 点击按钮
button.click()

time.sleep(2)

# 滑到底部
js_button = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_button)

time.sleep(3)

# 获取下一页的按钮
next = browser.find_element_by_xpath('//a[@class="n"]')

# 点击下一页
next.click()

time.sleep(2)

# 回到上一页
browser.back()

time.sleep(2)

# 回去
browser.forward()

time.sleep(3)

# 退出
browser.quit()