# _*_ coding : utf-8 _*_
# @Time : 2022/2/27 21:36
# @Author : 李洋
# @File : db
# @Project : test_毕设

import pymysql

'''
    常用模块：读写MYSQL
'''


def get_connection():
    '''
    获取MYSQL的连接
    :return: mysql connection
    '''

    return pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='itheima',  # 改成自己想操作的数据库
        charset='utf8mb4',
    )


def query_data(sql):
    '''
    根据SQL查询数据并且返回
    :param sql: SQL语句
    :return: list[dict]
    '''
    connection = get_connection()
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        # 别忘了关闭连接
        connection.close()


def insert_or_update_data(sql):
    '''
    执行新增insert或者updata的sql
    :param sql: insert or updata sql
    :return: 不返回内容
    '''
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        # 注意这里，只有commit才可以生效
        connection.commit()
    finally:
        # 别忘了关闭连接
        connection.close()
