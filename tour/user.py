from database import Base
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), unique=True, index=True)
    country = Column(String(100))
    email = Column(String(200))
    hashed_password = Column(String(512))

        