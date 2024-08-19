#Request

# 1. 경로 매개변수 (get)
# 2. 쿼리 매개변수 (get)
# 3. 바디 매개변수 (post, put, delete)

# http protocol request

# method : post, get, put, delete
# url : 서버주소
# headers : 인증, 쿠키, 세션, referral
# body : 데이터

#qeury parameter

from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/users")
def read_users(q: str = Query(None, max_length=50)):
    return {"q" : q}

@app.get("/items")
def read_items(internal_query: str = Query(None, alias='search')):
    return {'query_handled : ',internal_query}

@app.get('/users1')
def read_users(q : str = Query(None, deprecated=True)):
    return {"q" : q}

@app.get("/info")
def read_info(info : str = Query(None, description = '마 저오 입력해라 개쉐이야')):
    return {"info":info}

@app.get('/users1')
def read_users(q : str = Query(None, deprecated=True)):
    return {"q" : q}

@app.get('/items1')
def read_items(
    string_query : str = Query(default='zero value', min_length=2, max_length=5, regex="^[a-zA-Z]+$", title='String Query',example='abc'),
    number_query : float = Query(default=1.0 ,ge=0.5, le=10.5, title="Num Query", example=5.5) 
    ):
    return {
        "String Query" : string_query,
        "Num Query" : number_query
        }