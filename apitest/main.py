#coding:utf-8
from flask import Blueprint,request,jsonify
import requests
import hashlib
import random
import time
import os

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
    return jsonify({"sts":0,"msg":res.text,"time":res.elapsed.microseconds/1000})

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
    resp = requests.get(url,params=params)
    return jsonify(resp.json())

@api.route("/save",methods=["POST"])
def save():
    html = request.form.get("html")
    md = request.form.get("md")
    filename = request.form.get("filename")

    if len(filename)<3:
        filename = str(int(time.time()))

    htmlfile = filename+".html"
    mdfile = filename+".md"

    with open("./templates/"+htmlfile,"w",encoding="utf-8") as f:
        f.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>在线md文档</title><link rel="stylesheet" href="/static/style.css"><link rel="stylesheet" href="/static/preview.css"><style type="text/css">body{padding-top:2%;padding-left:20%;padding-right:20%;padding-bottom:2%;}</style></head><body>')
        f.write(html)
        f.write('</body></html>')
        f.close()

    with open("./md/"+mdfile, "w", encoding="utf-8") as f:
        f.write(md)
        f.close()

    return jsonify({"sts":0,"url":"/html/"+htmlfile})

@api.route("/load",methods=["GET"])
def load():
    md = request.args.get("md")
    mdStr = open("./md/"+md,encoding="utf-8").read()
    return jsonify({"sts":0,"msg":mdStr})


@api.route("/get_md_list",methods=["GET"])
def get_md_list():
    md_list = os.listdir("./md/")
    return jsonify({"sts":0,"msg":md_list})
