#!/usr/bin/env  python
#coding:utf-8

from flask import request,session,redirect
from functools import wraps
import hashlib,MySQLdb

conn = MySQLdb.connect(host='10.16.48.81',user='root',passwd='123',db='test',charset='utf8')
cur = conn.cursor()

def flask_auth(func):
    '''
    定义一个装饰器用于装饰需要验证的页面
    装饰器必须放在route装饰器下面
    '''
    # 定义包装函数
    @wraps(func) #消除自定义装饰器 改变原函数属性的副作用
    def wrapper(*args, **kargs):
        try:
            if func.__name__ == "index":
                if session['username']:
                    return func(*args,**kargs)
                else:
                    # 否则则重定向到登录页面
                    return redirect('/login/')
            else:
                if session['username'] and auth_def(func.__name__,session['username']):
                     return func(*args,**kargs)
                else:
                    return redirect('/unauth/')
        except:
            return redirect('/login/')
    return wrapper

def auth_pwd(pwd):
    #用户密码使用sha1加密 数据库不存储明文密码
    pd = (hashlib.sha1(pwd).hexdigest(),)
    sql = "select username from admin where password_hash = '%s'" %pd
    cur.execute(sql)
    if 0 < len(cur.fetchall()):
        return True
    return False

def auth_def(fn,user):
    sql = "select username from auth where defname = '%s'" %fn
    cur.execute(sql)
    if 0 < len(cur.fetchall()) and user == cur.fetchall()[0][0]:
        return True
    return False
