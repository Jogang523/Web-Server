# pip install sqlalchemy==1.4.39
# pip install pymysql==1.1.0

# create database fastapi_db;

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base  # => table 생성
from pydantic import BaseModel  # => pydantic model : 새로운 데이터타입 묶음

database_url = "mysql+pymysql://root:1234@localhost/fastapi_db" # 데이터베이스 주소
engine = create_engine(database_url)  # 데이터베이스 연결 객체

Base = declarative_base() # 테이블을 생성하기 위한 sqlalchemy 객체

# database architecture : database schema

# 테이블 생성 => 객체 => row data 하나
class User(Base): 
    __tablename__ = "users"  # 테이블이름..
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(120))

# pydantic model : 새로운 데이터 타입의 덩어리 - json data구조 생성
class UserCreate(BaseModel):
    username: str
    email: str

# session 객체를 만드는 첫 번쨰 방식 : 일반적이고 권장되는 방식
# database session 생성하고 관리하는 database 세션 객체..
# 장점 : session의 생명주기를 자동으로 관리 - 자원의 효율성을 높인다..
def get_db():
    db = Session(bind=engine)
    try:
        yield db   # generate함수 - database 객체를 return함
    except:
        db.close()  

# 테이블 생성 명렁 : 테이블이 없으면 새로 생성, 있으면 생성하지 않늠..
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : 'hello, world'}

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)): # 의존성 주입함수 - routing함수 실행 전 실행됨
    # 테이블 내에 있는 개별 데이터...
    new_user = User(username=user.username, email = user.email)  # 테이블 클래스의 객체는 table의 개별 row data
    db.add(new_user)  # db session 객체 테이블에 데이터 추가
    db.commit()  # db 변경사항저장
    db.refresh(new_user)  # db정보로  session db객체 정보를 update
    return {"id": new_user.id, "username":new_user.username, 'email':new_user.email}


# http://127.0.0.1:8000/users
# body
# {
#   "username" : "park",
#   "email" : "park@hanmail.net"
# }