from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student_list')
def student_list():
    stu_name = request.args.get('stu_name')
    stu_list = db.get_student_list(stu_name)

    return stu_list

if __name__== "__main__":
    app.run(host='127.0.0.1',port='8080')