from flask import Flask, render_template

import requests
from bs4 import BeautifulSoup

import crawling as cr

app = Flask(__name__)

@app.route('/about')
def about():
    return "네이트, 오늘의 유머, 클리앙의 베스트 콘텐츠를 보여줍니다"

@app.route('/contents')
def contents():
    mynate_title,nate_url = cr.nate()
    # myhumor = cr.today_humor()
    # myclient = cr.client()
    # print('0 :', mynate[0])
    # print()
    # print()
    # print('1 :', mynate[1])

    # return render_template('today_contents.html', list1=mynate, list2=myhumor, list3=myclient)
    return render_template('today_contents.html', nate_url=nate_url, nate_title=mynate_title, nate_len = len(mynate_title))



if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080')