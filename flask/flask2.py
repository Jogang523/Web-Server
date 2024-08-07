# jinaj2 template
# flask에서 jinja2 template을 이용해서 html을 구현한다
# jinja2 - html 내에서 python code를 실행시키는 방식,,,

from flask import Flask, render_template

app = Flask(__name__)

# flask가 client로부터 값을 받는 방식
# 1. 경로 - sub 경로를 통해서
# 2. get - url 내에서 ?
# 3. post - 별도의 변수에 값을 전달 

@app.route('/hello_park') # sub경로에서 값을 받는 경우
def hello_name1():
    return render_template('variable.html')

@app.route('/hello/<user>') # sub경로에서 값을 받는 경우
def hello_name2(user):
    return render_template('variable1.html',name=user)

if __name__=='__main__':
    app.run(host='127.0.0.1',port='8080')