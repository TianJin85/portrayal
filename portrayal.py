# -*-coding:utf-8 -*-
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():



    return url_for('static', filename='mask_wordcloud1.png')



if __name__ == "__main__":
    app.run()
