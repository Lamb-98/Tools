# _*_ coding : utf-8 _*_
# @Time : 2022/1/14 16:39
# @Author : 李洋
# @File : 70_解析_xpath的基本使用
# @Project : Python爬虫

from lxml import etree

# xpath解析
# （1）本地文件                                              etree.parse
# （2）服务器响应的数据 response.read().decode('utf-8')        etree.HTML()

tree = etree.parse('70_解析_xpath的基本使用.html')

# tree.xpath('xpath路径')

# 查找ul下面的li
# li_list = tree.xpath('//body/ul/li')

# 查找所有有id属性的li标签
# text()获取标签中的内容
# li_list = tree.xpath('//body/ul/li[@id]/text()')

# 找到id为h1的li标签 单引号里头要有字符串要用双引号
# li_list = tree.xpath('//ul/li[@id="h1"]/text()')

# 查找到id为h1的li标签的class的属性值
# li = tree.xpath('//ul/li[@id="h1"]/@class')

# 查询id中包含h的li标签
# li_list = tree.xpath('//ul/li[contains(@id,"h")]/text()')

# 查询id的值以h开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id,"h")]/text()')

# 查询id为h1和class为c1的li标签
# li_list = tree.xpath('//ul/li[@id="h1" and @class="c1"]/text()')

# 查询id为h1或l1的li标签
li_list = tree.xpath('//ul/li[@id="h1"]/text() | //ul/li[@id="l1"]/text()')

print(li_list)

