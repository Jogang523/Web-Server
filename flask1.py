from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('user_name') # get방식 파라미터 user_name값을 받음

    if username=='dave':
        data={'auth':'success'}
    else:
        data={'auth':'failed'}
    return jsonify(data) # rest api : json data

@app.route('/login_page')
def hello_html():
    return render_template('login.html') # render_template : html seript file을 return

if __name__=='__main__':
    app.run(host='0.0.0.0',port='8080')

# client가 server에게 요청(request)하는 방식

# 1. get 방식 :
# server에게 값을 전달 할 경우 - url에 파라미터 방식으로 전달
# 전달하는 값을 url에서 확인할 수 있음 - 보안에 취약
# url = "https://www.daum.net/news/search?q='빅데이터'&p=10"
# res = request.get(url)


# 2. post 방식 : 
# server에게 값을 전달 할 경우 - 별도의 데이터를 암호화해서 전달
# 전달하는 값을 url에서 확인할 수 없음 - 보안에 유리
# url = "https://www.daum.net/news/search",data={'query':'빅데이터','page':10}
# res = request.post(url,data=data)
