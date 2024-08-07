# 검색어와 페이지를 클리이언트로부터 서버가 받은 후 
# daum news에서 크롤링 결과를 리턴하는 웹서버를 생성하시오..
# get방식으로 구현하시오..

from flask import Flask, render_template, request
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

@app.route('/')
def hello_workd():
    return render_template('index.html')


@app.route('/daum_news')
def result():
    keyword = request.args.get('keyword')
    page_num = request.args.get('page')

    daum_news_titles = []
    
    daum_news_url = 'https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q={}&p={}'
    
    driver = webdriver.Chrome()
    
    for page in range(1, int(page_num)+1):
        url = daum_news_url.format(keyword, page)  

        print(url)
        driver.get(url)
        time.sleep(2)
    
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
    
        title_path = '#dnsColl > div:nth-child(1) > ul > li > div.c-item-content > div.item-bundle-mid > div.item-title > strong > a'
    
        for li in soup.select(title_path):
            # print(li.text)
            daum_news_titles.append(li.text)
        
    return render_template('daum_news.html', daum_news = daum_news_titles)





if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080')

