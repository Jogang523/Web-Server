#검색어와 페이지를 서버가 받은 후 daum news에서 크롤링 결과를 리턴하는 웹서버를 생성하시오

from flask import Flask, render_template, request
import  selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def hello_worked():
    return render_template('welcome.html')

@app.route('/daum_news')
def daum_serch():
    keyword = request.args.get('keyword')
    page_num = request.args.get('page_num')




if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')