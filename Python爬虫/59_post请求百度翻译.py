# _*_ coding : utf-8 _*_
# @Time : 2022/1/12 17:04
# @Author : 李洋
# @File : 59_post请求百度翻译
# @Project : Python爬虫

import urllib.request
import urllib.parse
import json


url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'Accept': '*/*',
    # 必须注释掉
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '117',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 关键是Cookie
    'Cookie': 'BIDUPSID=B28BC0504644F37405B3EAA84069B73C; PSTM=1640668375; BAIDUID=B28BC0504644F374F07B737A72199903:FG=1; BDUSS=RCVlpDc0VDaHlTdEtUZll6RFZ6eFRWdkgtQS15S1lDSjhrSUxzTzRlejFkQU5pRVFBQUFBJCQAAAAAAAAAAAEAAADVrzXTsKLA6779YwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPXn22H159thTU; BDUSS_BFESS=RCVlpDc0VDaHlTdEtUZll6RFZ6eFRWdkgtQS15S1lDSjhrSUxzTzRlejFkQU5pRVFBQUFBJCQAAAAAAAAAAAEAAADVrzXTsKLA6779YwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPXn22H159thTU; BDRCVFR[S4-dAuiWMmn]=FZ_Jfs2436CUAqWmykCULPYrWm1n1fz; delPer=0; PSINO=1; BDRCVFR[3iF-CRdS3ws]=mk3SLVN4HKm; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[CLK3Lyfkr9D]=mk3SLVN4HKm; RT="z=1&dm=baidu.com&si=dllgvfhoc7j&ss=kyb88z8t&sl=4&tt=7bq&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=ta4&ul=2esq&hd=2etx"; H_PS_PSSID=; BA_HECTOR=20002k2l052h00alub1gtt6f90q; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_0_2=1',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': '0c4beea2f37c628e0054f63fe87d3443',
    'domain': 'common'
}
# post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象的定制
# post请求的参数 是不会拼接再url的后面的，而是需要放在请求对象定制的参数中
# post请求的参数 必须要进行编码
request = urllib.request.Request(url=url, data=data, headers=headers)


# 模拟浏览器访问
response = urllib.request.urlopen(request)

# 获取响应内容
content = response.read().decode('utf-8')
print(content + '\n')
obj = json.loads(content)  # 转化成列表
print(obj)