from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

database_url = "mysql+pymysql://root:1234@localhost/fastapi_db"
engine = create_engine(database_url)

Base = declarative_base()

# database architecture : database schema

# 테이블 생성
class User(Base):
    __tablename__ = "users" # 테이블이름
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(120))

# pydantic model : 새로운 데이터 타입의 덩어리
class UserCreate(BaseModel):
    username : str
    email : str

# database session 생성하고 관리하는 의존성 함수
def get_db():
    db = Session(bind=engine)
    try:
        yield db # generate
    except:
        db.close()

# 테이블 생성 명령 : 테이블이 없으면 생성하고 있으면 생성 취소
Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
def read_root():
    return {"message":"hello python"}

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # 테이블 내에 있는 개별 데이터
    new_user = User(username=user.user.name, email = user.email)
    db.add(nwe_user)
    db.commit()
    db.refresh(new_user)
    return {"id" : new_user.id, "username" : new_user.username, "email" : new_user.email}

