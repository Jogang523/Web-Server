from pydantic import BaseModel
from typing import Optional

# 회원가입시 데이터 검증
class UserCreate(BaseModel):
    username: str
    email: str
    country: str
    password: str # 해시전 패스워드 받음
    

# 회원로그인시 데이터 검증
class UserLogin(BaseModel):
    username: str
    password: str # 해시전 패스워드 받음

class BoardCreate(BaseModel):
    subject: str
    content: str

class BoardUpdate(BaseModel):
    subject: Optional[str] = None
    content: Optional[str] = None