from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from typing import List
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory='templates')  # template folder 객체 생성

app.mount("/img", StaticFiles(directory='static/images'), name='img')

class ItemList(BaseModel):
    items : List[str]

@app.get("/")
def read_root(request: Request):  # Request : 클라이언트가 서버에 요청하는 다양한 정보를 가진 객체
    return templates.TemplateResponse("index.html", {"request":request})  # html script를 리턴, request객체도 포함

@app.get("/user/{username}")
def get_user(request: Request, username: str):
    return templates.TemplateResponse("index.html", {"request":request, "username":username})

@app.get("/greet")
def greeting(request: Request, time_of_day: str): # query 매개변수
    return templates.TemplateResponse("index1.html", {"request": request, "time_of_day":time_of_day})

@app.get("/items/")
def read_items(request: Request, my_items:List[str] = Query(...)):
    return templates.TemplateResponse("index2.html", {'request':request, 'items': my_items})

@app.post("/items")
def read_items(request: Request, items_list: ItemList):
    return templates.TemplateResponse("index2.html", {'request':request, 'items': items_list.items})

@app.get("/inherit")
def read_items(request: Request):
    return templates.TemplateResponse("index3.html", {'request':request})

@app.get("/bird")
def read_items(request: Request):
    return templates.TemplateResponse("index4.html", {'request':request})