from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from passlib.context import CryptContext
from starlette.middleware.sessions import SessionMiddleware


# fastapi 설정 -------------------

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_password_hash(password):        
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key = "fastapi_session_secret_key")

templates = Jinja2Templates(directory="templates")

DATABASE_URL = "mysql+pymysql://root:1234@localhost/memo_db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()


# schemas -----------------------------------

class Memo(Base):
    __tablename__ = 'memo'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    content = Column(String(1000))
    user_id= Col

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    email = Column(String(200))
    hashed_password = Column(String(512))

    
# table data type : pydantic ----------------------------

class MemoCreate(BaseModel):
    title: str
    content: str
    
class MemoUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

# 회원 가입
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# 로그인
class UserLogin(BaseModel):
    username: str
    password: str


# database session ---------------------------

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()
        
Base.metadata.create_all(bind=engine)
    


# routing(Contrller), crud ------------------------------------------------------


# 메모 관련 controller ------------ 회원만 접근이 가능하도록...

# 메모 생성
@app.post("/memos")
async def create_memo(request: Request, memo: MemoCreate, db: Session = Depends(get_db)):

    username = request.session.get("username") # 로그인 여부 확인
    if username is None:
        raise HTTPException(status_code = 401, detail = 'Not valid')
    
    user = db.query(User).filter(User.username == username).first()
    if user is None: # 회원가입 여부 확인
        raise HTTPException(status_code = 401, detail = 'Not valid')
    
    new_memo = Memo(user_id=user.id, title=memo.title, content=memo.content)
    db.add(new_memo)
    db.commit()
    db.refresh(new_memo)
    return ({"id": new_memo.id, "title": new_memo.title, "content": new_memo.content})

# 메모 조회
@app.get("/memos")
async def list_memos(request: Request, db: Session = Depends(get_db)):

    username = request.session.get("username") # 로그인 여부 확인
    if username is None:
        raise HTTPException(status_code = 401, detail = 'Not valid')
    
    user = db.query(User).filter(User.username == username).first()
    if user is None: # 회원가입 여부 확인
        raise HTTPException(status_code = 401, detail = 'Not valid')

    memos = db.query(Memo).filter(Memo.user_id==user.id).all()
    return templates.TemplateResponse("memos.html",{"request":request, "memos":memos})

# 메모 수정
@app.put("/memos/{memo_id}")
async def update_memo(request: Request, memo_id: int, memo: MemoUpdate, db: Session = Depends(get_db)):

    username = request.session.get("username") # 로그인 여부 확인
    if username is None:
        raise HTTPException(status_code = 401, detail = 'Not valid')
    
    user = db.query(User).filter(User.username == username).first()
    if user is None: # 회원가입 여부 확인
        raise HTTPException(status_code = 401, detail = 'Not valid')

    db_memo = db.query(Memo).filter(Memo.id == memo_id, Memo.user_id == user.id).first()

    if db_memo is None:
        return ({"error": "Memo not found"})

    if memo.title is not None:
        db_memo.title = memo.title
    if memo.content is not None:
        db_memo.content = memo.content
        
    db.commit()
    db.refresh(db_memo)
    return ({"id": db_memo.id, "title": db_memo.title, "content": db_memo.content})

# 메모 삭제
@app.delete("/memos/{memo_id}")
async def delete_memo(request: Request, memo_id: int, db: Session = Depends(get_db)):

    username = request.session.get("username") # 로그인 여부 확인
    if username is None:
        raise HTTPException(status_code = 401, detail = 'Not valid')
    
    user = db.query(User).filter(User.username == username).first()
    if user is None: # 회원가입 여부 확인
        raise HTTPException(status_code = 401, detail = 'Not valid')

    db_memo = db.query(Memo).filter(Memo.id == memo_id,Memo.user_id==user.id).first()

    if db_memo is None:
        return ({"error": "Memo not found"})
        
    db.delete(db_memo)
    db.commit()
    return ({"message": "Memo deleted"})


# 사용자 관련 controller ----------------------------------------------
# 회원가입, 로그인, 로그아웃

# 회원가입 - database
@app.post("/signup")
async def signup(signup_data: UserCreate, db: Session= Depends(get_db)):
    hashed_password = get_password_hash(signup_data.password)
    new_user = User(username=signup_data.username, email = signup_data.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"created successfully", "user_id":new_user.id}

# 로그인 - session
@app.post("/login")
async def login(request: Request, signin_data: UserLogin, db: Session=Depends(get_db)):

    # 회원여부검증
    user = db.query(User).filter(User.username == signin_data.username).first()
    if user and verify_password(signin_data.password, user.hashed_password):  # 회원이고 비밀번호가 유효
        request.session['username'] = signin_data.username
        return {"message" : "Logged in successfully"}
    else:
        raise HTTPException(status_code=401, detail='Invalid credential')
    
# 로그아웃
@app.post("/logout")
async def logout(request : Request):
    request.session.pop("username",None)
    return {"message" : "logged out..."}



# 기존 라우트 controller
@app.get('/')
async def read_root(request: Request):
    return templates.TemplateResponse('home.html', {"request": request})

@app.get("/about")
async def about():
    return {"message": "이것은 마이 메모 앱의 소개 페이지입니다."}
