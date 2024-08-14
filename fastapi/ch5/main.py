# Response Class
# http가 응답하는 종류를 정의하는 클래스
# 반환되는 데이터 형식을 제어

# respone_model => ptdantic model
# respone_class => respone_model

# 1. JSONResponse
# Json 형식의 데이터 반환 용도
# 2. HTMLResponse
# HTML 형식의 데이터 반환 용도
# 3. PlainTextResponse
# 단순 텍스트 형식의 응답 반환
# 4. RedirectResponse
# 클라이언트를 다른 url로 리다이렉션

from fastapi import FastAPI
from fastapi.responses import JSONResponse,HTMLResponse,PlainTextResponse,RedirectResponse

app = FastAPI()

@app.get('/json', response_class=JSONResponse)
def read_json():
    return {"msg":"this is JSON"}

@app.get("/html", response_class=HTMLResponse)
def read_html():
    return "<h1> This is html </h1>"

@app.get('/text', response_class= PlainTextResponse)
def read_text():
    return "this is text"

@app.get('/redirect', response_class=RedirectResponse)
def read_text():
    return RedirectResponse(url='/text')

