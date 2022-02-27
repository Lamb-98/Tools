# _*_ coding : utf-8 _*_
# @Time : 2022/2/9 14:07
# @Author : 李洋
# @File : 87_requests_cookie登陆古诗文网
# @Project : Python爬虫

#
# __VIEWSTATE_VIEWSTATE: ctExWKkM+XTZUFTydjBCnv9utWF3/b5fIflGNhQgHowDoVUKtiVtzQIWJ8gCBnCe5KbC2+bpQhcFbKYeqywpjY29/geSlQf0QNIpyOvs8pTTiJ1lt+Bl5fY8Jdo=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 779533783@qq.com
# pwd: 15515656
# code: 9YU2
# denglu: 登录
#
# 我们观察到VIEWSTATE VTEWSTATEGENERATOR code是一个可以变化的量
# _VIEWSTATE VIEWSTATEGENERATOR 一般情况看不到的数据都是在页面的源码中
# 我们观察到这两个数据在页面的源码中,所以我们需要获取页面的源码然后进行解析就可以获取了


import requests

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

# 获取页面的源码
response = requests.get(url=url, headers=headers)
content = response.text
print(content)
