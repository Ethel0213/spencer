from flask import Flask, render_template, request
from datetime import datetime
from waitress import serve
app = Flask(__name__)

@app.route("/")

def index():
	X = "作者溫凱升<br>"
	X +="<a href=/db>課程網頁</a><br>"
	X +="<a href=/spencer?nick=spencer>個人介紹及系統時間</a><br>"
	X +="<a href=/account>傳單</a><br>"
	return X

@app.route("/db")

def db():

	return "<a href= 'https://www.youtube.com/'>海青班資料庫管理</a>"

@app.route("/spencer",methods=["GET", "POST"])

def spencer():
	now = str (datetime.now())
	user = request.values.get("nick")
	return render_template("spencer.html", datetime=now, name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

#if __name__ == "__main__":

	#app.run()

	#serve(app, host='0.0.0.0', port=8080)