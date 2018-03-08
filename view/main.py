from flask import Blueprint,render_template
import requests

view = Blueprint("view",__name__)
req = requests.Session()

@view.route("/apitest",methods=["GET","POST"])
def apiview():
    return render_template("api.html")

@view.route("/md",methods=["GET","POST"])
def mdview():
    return render_template("md.html")

@view.route("/html/<filename>",methods=["GET","POST"])
def htmlview(filename):
    return render_template(filename)