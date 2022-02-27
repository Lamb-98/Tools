# _*_ coding : utf-8 _*_
# @Time : 2022/1/15 19:27
# @Author : 李洋
# @File : 72_解析_站长素材
# @Project : Python爬虫

# response中第一页
# https://sc.chinaz.com/tupian/meinvtupian.html

# https://www.pixiv.net/tags/%E3%81%8B%E3%81%90%E3%82%84%E6%A7%98/artworks

# https://www.pixiv.net/tags/%E3%81%8B%E3%81%90%E3%82%84%E6%A7%98/artworks?p=2

# 第二页
# https://sc.chinaz.com/tupian/meinvtupian_2.html
import urllib.request
from lxml import etree


def create_request(page):
    if page == 1:
        url = 'https://www.pixiv.net/tags/%E3%81%8B%E3%81%90%E3%82%84%E6%A7%98/artworks'
    else:
        url = 'https://www.pixiv.net/tags/%E3%81%8B%E3%81%90%E3%82%84%E6%A7%98/artworks?p=' + str(page)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content


def down_load(content):
    # 下载图片
    tree = etree.HTML(content)

    name_list = tree.xpath('//div[@id="root"]//img/@alt')

    # 一般设计图片的网站都会进行懒加载，要用没显示完时的src
    src_list = tree.xpath('//div[@id="root"]//img/@src')

    for i in range(len(name_list)):
        name = name_list[i]

        src = src_list[i]

        url = 'https:' + src

        print(name,url)
        # urllib.request.urlretrieve(url=url, filename='./kaguya/' + name + '.jpg')


start_page = int(input('请输入起始页码：'))
end_page = int(input('请输入结束页码：'))

for page in range(start_page, end_page + 1):
    # 请求对象的定制
    request = create_request(page)
    # 获取网页的源码
    content = get_content(request)
    # 下载图片
    down_load(content)
