# client - 서버에 요청을 하는 주체
# server - 클라이언트의 요청을 받고 요청에 맞는 데이터를 리턴하는 주제

# http 메소드 (client가 server에게 요청을 하는 메소드)
# 1. get -서버로 요청 시 url에 경로 매개변수, 쿼리 매개변수 방식으로 전달
# 2. post - 서버에 요청시 전송값을 별도의 json형식으로 암호화 후 전달
# 3. put - 서버에 값의 변경을 요청하는 경우
# 4. delete - 서버에 값의 삭제를 요청하는 경우

from fastapi import FastAPI
app = FastAPI()

# 파라미터 없이 get 요청
@app.get('/')
def read_root():
    return {'message':'hello, fastapi'}

# 경로 파라미터를 통해서 get 요청
@app.get('/items/{item_id}')
def read_item(item_id : int):
    return {'item_id' : item_id}

# 쿼리 파라미터를 통해서 요청
@app.get('/items1')
def read_item(item_id : int):
    return {'item_id' : item_id}

# 쿼리 파라미터를 통해서 요청2
@app.get('/items2')
def read_item(skip : int = 0, limit : int = 10):
    return {'skip' : skip,'limit' : limit}

# post요청을 받는 경우
# http://127.0.0.1:8000/items/
# {
#   "test" : "fastapi", 
#   "value":40
# }
@app.post('/items/')
def create_item(item : dict):
    return {'item' : item}

# put 요청
@app.put('/items/{item_id}')
def read_item(item_id : int, item : dict):
    return {'item_id' : item_id, 'updataed_item' : item}

#delete 삭제 요청
@app.delete('/items/{item_id}')
def delete_item(item_id: int):
    return {'message' : f"Item {item_id} deleted..."}