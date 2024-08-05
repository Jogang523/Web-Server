from flask import Flask
import requests

app = Flask(__name__)

@app.route('/google')
def get_google():
    res = requests.get('https://www.google.co.kr')
    return res.text

@app.route('/naver')
def get_naver():
    res = requests.get('https://www.naver.co.kr')
    return res.text

@app.route('/daum')
def get_daum():
    res = requests.get('https://www.daum.net')
    return res.text

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')