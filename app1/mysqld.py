#!/usr/bin/env	python
#coding:utf-8
__author__ = "zhangjun"

import MySQLdb

conn = MySQLdb.connect(host='10.16.48.81',user='root',passwd='123',db='weblog',charset='utf8')
cur = conn.cursor()

def getData(num=0):
    try:
        conn.ping()
    except:
        conn = MySQLdb.connect(host='10.16.48.81',user='root',passwd='123',db='weblog',charset='utf8')
        cur = conn.cursor()
    sql = "select ip,n_ip,c_room,operator,status from download_nginx_copy limit %s,10;" %num
    cur.execute(sql)
    data = cur.fetchall()
    return data

def serData(ip):
    try:
        conn.ping()
    except:
        conn = MySQLdb.connect(host='10.16.48.81',user='root',passwd='123',db='weblog',charset='utf8')
        cur = conn.cursor()    
    sql = "select ip,n_ip,c_room,operator,status from download_nginx_copy where ip LIKE '%%%s%%'" %ip
    cur.execute(sql)
    data = cur.fetchall()
    return data

def delData(ip):
    try:
        conn.ping()
    except:
        conn = MySQLdb.connect(host='10.16.48.81',user='root',passwd='123',db='weblog',charset='utf8')
        cur = conn.cursor()
    sql = "delete from download_nginx_copy where ip = '%s';" %ip
    cur.execute(sql)

def modData(ip,status):
    try:
        conn.ping()
    except:
        conn = MySQLdb.connect(host='10.16.48.81',user='root',passwd='123',db='weblog',charset='utf8')
        cur = conn.cursor()
    sql = "update download_nginx_copy set status = '%s' where ip = '%s';" %('unactive',ip)
    if status == "1":
        sql = "update download_nginx_copy set status = '%s' where ip = '%s';" %('active',ip)
    cur.execute(sql)

def addData(ip,n_ip,c_room,operator,status):
    try:
        conn.ping()
    except:
        conn = MySQLdb.connect(host='10.16.48.81',user='root',passwd='123',db='weblog',charset='utf8')
        cur = conn.cursor()    
    sql = "insert into download_nginx_copy (ip,n_ip,c_room,operator,status) values('%s','%s','%s','%s','%s')" %(ip,n_ip,c_room,operator,status)
    cur.execute(sql)
