# -*-coding:utf-8 -*-
from messageDB import message
from maker_portrayal import maker_pl

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/user/<int:user_id>')
def index(user_id):

    mess_text = message('localhost', 'root', 'root', 'userdb', 'utf8mb4').conn(user_id)  # 调用messageDB获取会员信息

    # 生成图片
    maker_pl.maker_png(mess_text, user_id)

    return 'static/user_img/user_id%d.png' %user_id

@app.errorhandler(404)
def page_not_found(error):

    return "没有此页面"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80', debug=True)
