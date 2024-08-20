from fastapi import FastAPI,Request,Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
templates = Jinja2Templates(directory = "templates")

database_url="mysql+pymysql://root:1234@localhost/memo_db"
engine = create_engine(database_url)

Base = declarative_base()

# table
class Memo(Base):
    __tablename__ = "memo"
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String(100))
    content = Column(String(1000))

# ptdantic model - 새로운 데이터 모델(타입) - 유효성 검증, 편리성 - table 구조와 동일하게

class MemoCreate(BaseModel):
    title : str
    content : str

class MemoUpdate(BaseModel):
    title : Optional[str] = None
    content : Optional[str] = None

def get_db():
    db = Session(bind=engine) # database session 객체
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine) # 테이블 생성


@app.post("/memos")
async def create_memo(memo: MemoCreate, db: Session = Depends(get_db)):
    new_memo = Memo(title = memo.title, content = memo.content)
    db.add(new_memo)
    db.commit()
    db.refresh(new_memo)
    return ({"id":new_memo.id, "title":new_memo.title, "content":new_memo.content})

@app.get("/memos/")
async def list_memos(db:Session = Depends(get_db)):
    memos = db.query(Memo).all()
    return [{"id":memo.id,"title":memo.title,"content":memo.content} for memo in memos]

@app.put("/memos/{memo_id}")
async def update_memo(memo_id: int, memo: MemoUpdate, db : Session = Depends(get_db)):
    db_memo = db.query(Memo).filter(Memo.id == memo_id).first() 
    if db_memo is None:
        return ({"error":"memo is no found"})
    if memo.title is not None:
        db_memo.title = memo.title
    if memo.content is not None:
        db_memo.content = memo.content
    db.commit()
    db.refresh(db_memo)
    return ({"id":db_memo.id, "title":db_memo.title, "content":db_memo.content})

@app.delete("/memos/{memo_id}")
async def delete_memo(memo_id: int, db: Session = Depends(get_db)):
    db_memo = db.query(Memo).filter(Memo.id == memo_id).first() 
    if db_memo is None:
        return ({"error": "memo not found"})
    
    db.delete(db_memo)
    db.commit()
    return ({"message": "memo delete"})