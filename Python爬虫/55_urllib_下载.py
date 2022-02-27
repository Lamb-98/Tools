# _*_ coding : utf-8 _*_
# @Time : 2022/1/12 15:20
# @Author : 李洋
# @File : 55_urllib_下载
# @Project : Python爬虫

# 下载网页
import urllib.request

#
# url_page = 'http://www.baidu.com'
#
# urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片
url_img = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F202004%2F20%2F20200420094845_wpbrh.thumb.1000_0.png&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1644564484&t=a87165dfaf06de9da581a45647516533'

urllib.request.urlretrieve(url_img, 'Nezuko.jpg')

# 下载视频
url_video = 'https://vd4.bdstatic.com/mda-mmh32assaxk7ag86/hd/cae_h264/1639794915266355279/mda-mmh32assaxk7ag86.mp4?v_from_s=hkapp-haokan-hna&auth_key=1641974700-0-0-b680ed0258024d6837f938edec2db73e&bcevod_channel=searchbox_feed&pd=1&pt=3&logid=2100285329&vid=11970505336980286062&abtest=100254_1&klogid=2100285329'
urllib.request.urlretrieve(url_video, 'Nezuko.mp4')
