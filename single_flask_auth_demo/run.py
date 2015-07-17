#!/usr/bin/env  python
#coding:utf-8

from flask import jsonify,request,render_template,redirect,Flask
from datetime import timedelta
from mysqld import *
from mongo import *
from auth import *

app = Flask(__name__)
app.permanent = True
app.permanent_session_lifetime = timedelta(minutes=5)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
m = Mongo()

@app.route('/login/')
def login():
    return render_template("login.html")

@app.route('/unauth/')
def unauth():
    return "无权限！！！"

@app.route('/auth/',methods=['POST'])
def auth():
    data = request.form
    print data
    if auth_pwd(data['password']):
        session['username'] = data['username']
        return redirect('/')
    return render_template("login.html")

@app.route('/logout/')
def logout():
    # 如果会话中有用户名就删除它。
    session.pop('username', None)
    return redirect('/login/')

@app.route("/hchart",methods=['GET'])
@flask_auth
def highchart():
    ip = request.args.get('ip')
    if ip:
        data = m.search(ip)
        return  render_template("hchart.html",data=data,ip=ip)
    data = m.search("10.10.88.220")
    return render_template("hchart.html",data=data,ip="10.10.88.220")

@app.route("/")
@flask_auth
def index():
    data = getData()
    page = 1
    return render_template("index.html",data = data, num = page)

@app.route("/page",methods=['GET'])
def page():
    act = request.args.get('act')
    page = int(request.args.get('page'))
    if act == 'a':
        if page == 1:
            return redirect("/")
        else:
            page -= 1
            data = getData((page-1)*10)
            return render_template("index.html",data = data, num = page)
    if act == 'b':
        data = getData(page*10)
        page += 1
        if 10 > len(data):
            return render_template("index.html",data = data, num = page, point = 1)
        return render_template("index.html",data = data, num = page)

@app.route("/search_ip",methods=['GET'])
def search():
    ip = request.args.get("ip")
    result = serData(ip)
    return render_template("index.html",data = result, num = 0)

@app.route("/delete_ip",methods=['GET'])
def delete():
    ip = request.args.get("ip")
    delData(ip)
    return redirect("/")

@app.route("/mod",methods=['GET'])
def mod():
    ip = request.args.get("ip")
    status = request.args.get("status")
    modData(ip,status)
    return redirect("/")

@app.route("/add",methods=['GET'])
def add():
    ip = request.args.get("ip")
    n_ip = request.args.get("n_ip")
    c_room = request.args.get("c_room")
    operator = request.args.get("operator")
    status = request.args.get("status")
    addData(ip,n_ip,c_room,operator,status)
    return redirect("/")

@app.route("/test/")
def test():
    return render_template("test.html")

@app.route("/123/",methods=['POST'])
def xxxx():
    data = request.json
    print data['name']
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=10101)
