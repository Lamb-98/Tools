# _*_ coding : utf-8 _*_
# @Time : 2022/1/13 14:49
# @Author : 李洋
# @File : 62_ajax请求豆瓣电影前10页
# @Project : Python爬虫

import urllib.request
import urllib.parse


def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page, content):
    # with open('douban_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
    #     fp.write(content)
    fp = open('douban_' + str(page) + '.json', 'w', encoding='utf-8')
    fp.write(content)


# 开始
start_page = int(input('请输入起始页码：'))
end_page = int(input('请输入结束页码：'))

for page in range(start_page, end_page + 1):
    # 每一页的请求定制
    request = create_request(page)
    # 获取响应的数据
    content = get_content(request)
    # 下载
    down_load(page, content)
