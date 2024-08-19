from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
template = Jinja2Templates(directory='template')

app.mount("/img", StaticFiles(directory='static/image'), name='img')

@app.get('/')
def read_root(request: Request): # Request : 클라이언트가 서버에 요청하는 다양한 정보를 가진 객체
    return template.TemplateResponse("index.html",{"request":request}) # html script를 리턴, request 객체도 포함

@app.get("/user/{username}/")
def read_root(request: Request,username:str): # Request : 클라이언트가 서버에 요청하는 다양한 정보를 가진 객체
    return template.TemplateResponse("index.html",{"request":request,"username":username})

@app.get("/inherit")
def read_items(request: Request):
    return template.TemplateResponse("index3.html",{"request":request})

@app.get("/bird")
def read_items(request: Request):
    return template.TemplateResponse("index4.html",{"request":request})