from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func  # 자동 생성 시간 필드 추가
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), unique=True, index=True)
    country = Column(String(100))
    email = Column(String(200))
    hashed_password = Column(String(512))

class Board(Base):
    __tablename__ = "board"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    subject = Column(String(100), nullable=False)
    content = Column(Text(2000), nullable=False)
    create_date = Column(DateTime, server_default=func.now(), nullable=False)  # 자동 생성 시간


    comments = relationship("Coment", backref="board")  # 댓글과의 관계 설정

class Coment(Base):
    __tablename__ = "coment"

    id = Column(Integer, primary_key=True)
    content = Column(Text(2000), nullable=False)
    create_date = Column(DateTime, server_default=func.now(), nullable=False)  # 자동 생성 시간
    board_id = Column(Integer, ForeignKey("board.id"))  # 외래 키 설정 (게시글과 연결)
