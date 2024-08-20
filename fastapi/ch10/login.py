from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key='fastapi_secret_key')

class Item(BaseModel):
    username:str
    password:str

@app.post("/login")
# async def login(request: Request, username: str, password: str):
async def login(request:Request,user: Item):
    if user.username=='park' and user.password =='1234':
        request.session["username"] = user.username
        return {"message" : "successfully logeed in"}
    else:
        raise HTTPException(status_code=401, detail="invalid credential")
    
# 로그인 상대와 안한 상태의 화면이 다름    
@app.get("/dashboard/")
async def dashboard(request: Request):
    #쿠키에 저장된 
    username = request.session.get("username")
    if not username:
        raise HTTPException(status_code=401, detail= "not authorized")
    return {"message":f"welcome to the dashboard,{username}"}