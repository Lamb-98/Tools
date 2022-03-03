import os
import time
from langconv import *

'''获取文件名'''


def getname(rootdir, list_filename):
    for root, dirs, files in os.walk(rootdir, topdown=False):
        for name in files:
            list_filename.append(name)


'''繁体转简体'''
def cht_to_chs(rootdir, list_filename):
    for i in range(len(list_filename)):
        '''整理文件名'''
        filename = list_filename[i]
        name_list = filename.rsplit('.', 1)
        filename_e1 = name_list[0]  # 纯文件名
        filename_e2 = name_list[1]  # 文件后缀
        '''读取'''
        path1 = rootdir + filename
        f = open(path1, mode='r', encoding="utf-8")  # 文件对象
        str = f.read()
        print("读取文件：" + path1)
        f.close()
        '''转换'''
        str = Converter('zh-hans').convert(str)
        str.encode('utf-8')
        print("转换...")
        '''写入'''
        path2 = rootdir + filename_e1 + "_chs." + filename_e2
        fp = open(path2, mode='w+', encoding="utf-8")
        fp.write(str)
        fp.close()
        print("文件：" + path2 + "写入完成\n")
        time.sleep(0.05)  # io延迟


'''简体转繁体'''


def chs_to_cht(rootdir, list_filename):
    for i in range(len(list_filename)):
        '''整理文件名'''
        filename = list_filename[i]
        name_list = filename.rsplit('.', 1)
        filename_e1 = name_list[0]  # 纯文件名
        filename_e2 = name_list[1]  # 文件后缀
        '''读取'''
        path1 = rootdir + filename
        f = open(path1, mode='r', encoding="utf-8")  # 文件对象
        str = f.read()
        print("读取文件：" + path1)
        f.close()
        '''转换'''
        str = Converter('zh-hant').convert(str)
        str.encode('utf-8')
        print("转换...")
        '''写入'''
        path2 = rootdir + filename_e1 + "_cht." + filename_e2
        fp = open(path2, mode='w+', encoding="utf-8")
        fp.write(str)
        fp.close()
        print("文件：" + path2 + "写入完成\n")
        time.sleep(0.05)  # io延迟


def main():
    list_filename = []
    list_file = []
    print("简繁字幕转换工具，Creat By Kyon!")
    rootdir = input("请输入字幕目录路径：")+"\\"
    #rootdir = "../"  # D:/pytest/

    getname(rootdir, list_filename)

    #print("请在字幕文件目录中新建目录并将软件移入新目录")
    print("请选择转换类型\n"
          "1.繁体转简体\n"
          "2.简体转繁体\n"
          "其他：退出程序\n")
    flag = input("请输入：")
    if flag == "1":
        print("繁体转简体")
        cht_to_chs(rootdir, list_filename)
    elif flag == "2":
        print("简体转繁体")
        chs_to_cht(rootdir, list_filename)

    input("按任意键退出")


if __name__ == "__main__":
    main()
