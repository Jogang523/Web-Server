from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student_list')
def student_list():
    stu_name = request.args.get('stu_name') # get 요청시 url에서 값을 받아옴
    stu_list = db.get_student_list(stu_name)

    return render_template('student_list.html', data_list=stu_list)

@app.route('/student_info', methods=['GET', 'POST'])
def student_info():
    stu_idx = request.args.get('stu_idx')
    result_dic = db.get_student_info(stu_idx)
    result_list = db.get_point(stu_idx)
    
    return render_template('student_info.html', data_dic=result_dic, data_list=result_list)

@app.route('/add_point')
def add_point():
    stu_idx = request.args.get('stu_idx')
    temp_dic={}
    temp_dic = {'stu_idx': stu_idx}

    return render_template('add_point.html', data_dic=temp_dic)

@app.route('/add_point_pro', methods=['POST'])
def add_point_pro():
    point_stu_grade = request.form['point_stu_grade']
    point_stu_kor = request.form['point_stu_kor']
    point_stu_idx = request.form['point_stu_idx']
    db.add_point(point_stu_idx, point_stu_grade, point_stu_kor)  

    temp_dic = {'stu_idx': point_stu_idx}
    html = render_template('add_point_pro.html', data_dic=temp_dic)
    return html

@app.route('/add_student')
def add_student():
    return render_template('add_student.html')

@app.route('/add_student_pro', methods=['POST'])
def add_student_pro():  
    stu_name = request.form['stu_name']
    stu_age = request.form['stu_age']
    stu_addr = request.form['stu_addr']
    idx = db.add_student(stu_name, stu_age, stu_addr) 

    result_dic = {'stu_idx': idx}
    html = render_template('add_student_pro.html', data_dic=result_dic)
    return html

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080')
