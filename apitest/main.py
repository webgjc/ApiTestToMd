from flask import Blueprint,request,jsonify
import requests
import hashlib
import random
import time

api = Blueprint("api",__name__)
req = requests.Session()

@api.route("/api",methods=["GET","POST"])
def apiget():
    query = request.args.to_dict()
    body = request.form.to_dict()
    if query['method'] == "get":
        res = req.get(query['url'],params=body,timeout=3)
    elif query['method'] == "post":
        res = req.post(query['url'],data=body,timeout=3)
    elif query['method'] == "put":
        res = req.put(query['url'],data=body,timeout=3)
    elif query['method'] == "delete":
        res = req.delete(query['url'],data=body,timeout=3)
    return jsonify({"sts":"0","msg":res.text,"time":res.elapsed.microseconds/1000})

@api.route("/translate",methods=["GET"])
def trans():
    q = request.args['q']

    appid = '20160702000024420'
    secretKey = 'hEioJEDRhi1fbE0AO45q'
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    params={
        "q":q,
        "from":fromLang,
        "to":toLang,
        "appid":appid,
        "salt":salt,
        "sign":sign
    }
    print(params)
    resp = requests.get(url,params=params)
    return jsonify(resp.json())

@api.route("/save",methods=["POST"])
def save():
    html = request.form.get("html")

    filename = str(int(time.time()))+".html"

    with open("./templates/"+filename,"w",encoding="utf-8") as f:
        f.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>在线md文档</title><link rel="stylesheet" href="/static/style.css"><link rel="stylesheet" href="/static/preview.css"></head><body>')
        f.write(html)
        f.write('</body></html>')

    return jsonify({"sts":0,"url":"/html/"+filename})