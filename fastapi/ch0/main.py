# 웹프레임 워크
# 마이크로 프레임 워크 - 필수 적인 기능만 제공, 기타 기능은 외부 모듈이나 개발을 통해서 직접 구현 - flask / faskapi
# 풀 스택 프레임 워크, -django / springboot

# fastapi
# restful api 구현 최적화된 프레임 워크
# 비동기 처리를 기본으로 제공
# 속도가 빠르다..


from fastapi import FastAPI

app = FastAPI() # Fastapi 객체생성

# get 요청
@app.get('/') #routing
def read_root():
    return {'message':'hello world!'}

# nvicorn main:app --reload
# 문서를 자동 생성
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redocs


# 경로 파라미터(path parameters)
@app.get("/item/{item_id}")
def read_item(item_id):
    return {'item_id' : item_id}

# 쿼리 매개변수
# http://127.0.0.1:8000/items?skip=5&limit=10
@app.get('/items')
def read_items(skip, limit):
    return {'skip':skip,'limit':limit}