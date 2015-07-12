#!/usr/bin/env  python#coding:utf-8from flask import Flask,jsonify,request,render_template,redirectfrom mysqld import *from mongo import *app = Flask(__name__)app.debug = Truem = Mongo()@app.route("/hchart",methods=['GET'])def demo():    ip = request.args.get('ip')    if ip:        data = m.search(ip)        return  render_template("hchart.html",data=data,ip=ip)    data = m.search("10.10.88.220")    return render_template("hchart.html",data=data,ip="10.10.88.220")@app.route("/")def index():    data = getData()    page = 1    return render_template("index.html",data = data, num = page)@app.route("/page",methods=['GET'])def page():    act = request.args.get('act')    page = int(request.args.get('page'))    if act == 'a':        if page == 1:            return redirect("/")        else:            page -= 1            data = getData((page-1)*10)            return render_template("index.html",data = data, num = page)    if act == 'b':        data = getData(page*10)        page += 1        if 10 > len(data):            return render_template("index.html",data = data, num = page, point = 1)        return render_template("index.html",data = data, num = page)@app.route("/search_ip",methods=['GET'])def search():    ip = request.args.get("ip")    result = serData(ip)    return render_template("index.html",data = result, num = 0)@app.route("/delete_ip",methods=['GET'])def delete():    ip = request.args.get("ip")    delData(ip)    return redirect("/")@app.route("/mod",methods=['GET'])def mod():    ip = request.args.get("ip")    status = request.args.get("status")    modData(ip,status)    return redirect("/")@app.route("/add",methods=['GET'])def add():    ip = request.args.get("ip")    n_ip = request.args.get("n_ip")    c_room = request.args.get("c_room")    operator = request.args.get("operator")    status = request.args.get("status")    addData(ip,n_ip,c_room,operator,status)    return redirect("/")@app.route("/test/")def test():    return render_template("test.html")@app.route("/123/",methods=['POST'])def aaaa():    data = request.json    print data['name']    return jsonify(data)if __name__ == "__main__":    app.run(host="0.0.0.0",port=2324)