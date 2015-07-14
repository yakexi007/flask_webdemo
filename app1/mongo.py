#!/usr/bin/env  python
#coding:utf-8

import pymongo

class Mongo:
    def __init__(self):
        self.conn = pymongo.MongoClient(host="192.168.99.173")
        self.db = self.conn.log

    def search(self,ip):
        data = self.db.log.find({"host":"%s" %ip})
        data1 = self.db.connects.find({"host":"%s" %ip})
        result = [[int(x['timestamp']),x['out_s'],x['in_s']] for x in data]
        result1 = [[int(x['timestamp']),x['total']] for x in data1]
        return [result,result1]