# COSMiddleware
# 보안을 강화해주는 middleware
# api호출을 측정 ip에게만 허용...

# rest api
# open api - 모든 사람에게 개방
# closed api - 특정 client에게만 개방/ 내부 시스템 내에서 데이터를 transaction

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
def read_root():
    return {"message":"hello, fast api"}

@app.get('/hello')
def hello():
    return {"message":"hello, hello"}