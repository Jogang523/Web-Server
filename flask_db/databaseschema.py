import pymysql

conn=pymysql.connect(host='127.0.0.1',user='root',password='1234',charset='utf8')

# sql='show databases;'

cursor=conn.cursor()
# cursor.execute(sql)
# result=cursor.fetchall()

# print(result)

sql = 'create database if not exists flask_db;'
cursor.execute(sql)


# sql='show databases;'
# cursor.execute(sql)
# result=cursor.fetchall()

# print(result)

sql = 'use flask_db;'
cursor.execute(sql)

sql = 'drop table if exists member;'
cursor.execute(sql)

sql = """
create table if not exists member(
id int not null auto_increment,
userid varchar(50) not null,
pwd varchar(200) not null,
name varchar(20) default null,
email varchar(50) default null,
regdate datetime default null,
primary key (id));
"""

cursor.execute(sql)


sql = """
insert into member values
    (1, 'aaa', '1234', '아이유', 'aaa@aaa.co.kr', '2019-06-24 01:00:00'),
    (2, 'bbb', '1234', '방탄아미',' bts@army.co.kr', '2019-06-25 12:12:30');
"""
cursor.execute(sql)

sql = '''
select * from member;
'''

cursor.execute(sql)
result=cursor.fetchall()
print(result)

sql = 'drop table if exists point_table;'
cursor.execute(sql)

sql = '''
create table if not exists point_table(
`point_stu_idx` int default null,
`point_stu_grade` varchar(50) default null,
`point_stu_kor` varchar(50) default null
);
'''
cursor.execute(sql)


sql='''
insert into point_table values
(2, '2', '90'),
(2, '3', '95'),
(2, '1', '89')
'''
cursor.execute(sql)

sql = '''
select * from point_table;
'''

cursor.execute(sql)
result=cursor.fetchall()
print(result)

sql = 'drop table if exists student_table;'
cursor.execute(sql)


sql = '''
create table if not exists student_table(
`stu_idx` int not null auto_increment primary key,
`stu_name` varchar(50) default null,
`stu_age` varchar(3) default null,
`stu_addr` varchar(50) default null
);
'''
cursor.execute(sql)

sql='''
insert into student_table (`stu_name`, `stu_age`, `stu_addr`) values
('홍길동','18','서울시'),
('김개똥','19','서울시');
'''
cursor.execute(sql)

sql = '''
select * from student_table;
'''

cursor.execute(sql)
result=cursor.fetchall()
print(result)

conn.commit()
conn.close()