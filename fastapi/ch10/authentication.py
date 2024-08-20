# authentication
# 1. http 헤더 인증 정보를 전달 - 기초, 실제 사용 X
# 2. JWT 방식 - 사용자 상태를 유지 하지 않음 ,  client에서 정보를 저장, 서버에 부담이 없다, 확장시 복잡성이 없다.
# 3. Session - 상태 정보를 유지 O, client에서 사용자 정보 저장 - 서버에 부담, 확장 시 복잡

# client 서버에 요청
# client 정보 (ip, id, pw) + secret key => 암호화 => secret id => client에게 전달 => server에 request 시 secret id를 포함 = > 서버가 secret id를 통해서 request의 유효성 검증 & 사용자 정보 matching해서 사용자 정보를 관리 가능.

# 세션
# 1. 세션의 역할
# 웹에서 상태를 유지하는 방법
# http 프로토콜의 상태정보를 저장하지 못하는 문제를 해결

# 2. 작동 원리
# 첫 요청 시 서버는 클라이언트에 고유한 세션 id를 발급
# client session id를 cookie에 저장
# client가 srever에 요청 시 cookie에 secret id를 포함
# sercer에서 secret id를 검증 & 사용자 확인

# fastapi의 session 관리
# fastapi는 Starlette의 기능을 상속받아서 session관리를 한다.
# SessionMiddleware라는 middleware를 통해서 session 관리를 수행

from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key='fastapi_secret_key')

# secret_key : 최소 200자 이상, 환경변수에 저장, key를 관리하는 서비스, 반복적 수정

@app.post("/set")
async def set_session(request: Request):
    request.session["username"]="john"
    return {"message":"Session valur set"}

@app.get("/get")
async def get_session(request: Request):
    username = request.session.get('username','Guest')
    return {"username":username}