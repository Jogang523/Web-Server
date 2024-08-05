from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello_if/<int:score>")
def hello_html(score):
    return render_template('condition.html',score=score)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')