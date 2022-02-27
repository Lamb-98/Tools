# _*_ coding : utf-8 _*_
# @Time : 2022/2/8 14:52
# @Author : 李洋
# @File : 74_jsonpth_解析淘票票
# @Project : Python爬虫

import urllib.request

url = 'https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1644303385315_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ':authority': 'www.taopiaopiao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1644303385315_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 't=35d38b2eed6c2f8b2d6de75379faefac; _tb_token_=e77e31f63ae1b; cookie2=1aff20a7410ff8381f389f40162f8b9a; tb_city=510100; tb_cityName="s8m2vA=="; l=eBgrqt4eLO-DSo3vBO5aourza779gIOb8sPzaNbMiInca1JF9F_1NNCngYWJWdtjgt5bYeKPkdi_7RE6JS4_WVt8iqShee8CeiJw8e1..; isg=BN3d6ZCKY36fxwdSHPhVL_4n7LnX-hFM1kdzeZ-jCDRjVvyIZkq3Ho5IgErQlikE',
    'referer': 'https://www.taopiaopiao.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# split 切割（切完是列表）,切掉同为括号及其之前和之后的内容
content = content.split('(')[1].split(')')[0]

with open('74_jsonpth_解析淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

import json
import jsonpath

obj = json.load(open('74_jsonpth_解析淘票票.json', 'r', encoding='utf-8'))

city_list = jsonpath.jsonpath(obj,'$..regionName')

print(city_list)
