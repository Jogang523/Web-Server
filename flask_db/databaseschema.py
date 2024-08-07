
# database schema 설정 - 데이터베이스 구조 구성..

# pip install pymysql

import pymysql


# database server와 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', charset='utf8')

cursor = conn.cursor()


# 데이터베이스 생성 및 초기화

sql = "drop database if exists flask_db;"
cursor.execute(sql)

sql = 'create database if not exists flask_db;'
cursor.execute(sql)

sql = "use flask_db;"
cursor.execute(sql)


# table 생성 및 초기화

# member table

sql = 'drop table if exists member;'
cursor.execute(sql)

sql = """
create table if not exists member (
id int not null auto_increment primary key,
`userid` varchar(50) not null,
`pwd` varchar(200) not null,
`name` varchar(20) default null, 
`email` varchar(50) default null,
`regdate` datetime default null);
"""
cursor.execute(sql)

sql = """
insert into member values 
    (1, 'aaa', '1234', '아이유', 'aaa@aaa.co.kr', '2019-06-24 01:00:00'),
    (2, 'bbb', '1234', '방탄아미', 'bts@army.co.kr', '219-06-25 12:12:30');
"""
cursor.execute(sql)


# point_table

sql = 'drop table if exists point_table;'
cursor.execute(sql)

sql = """
create table if not exists point_table (
`point_stu_idx` int default null,
`point_stu_grade` varchar(50) default null,
`point_stu_kor` varchar(50) default null);
"""
cursor.execute(sql)

sql = """
insert into point_table values 
(2, '2', '90'),
(2, '3', '95'),
(3, '1', '89');
"""
cursor.execute(sql)

# student_table

sql = 'drop table if exists student_table;'
cursor.execute(sql)

sql = """
create table if not exists student_table (
`stu_idx` int not null auto_increment primary key,
`stu_name` varchar(50) default null,
`stu_age` varchar(3) default null,
`stu_addr` varchar(50) default null);
"""
cursor.execute(sql)

sql = """
insert into student_table values 
(1, '홍길동', '18', '서울시'),
(2, '김개똥', '19', '서울시');
"""
cursor.execute(sql)


conn.commit()
conn.close()

