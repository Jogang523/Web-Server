# type hint
# 변수나 함수의 예상되는 데이터 타입을 명시적으로 표현해서 요청의 유효성을 검증하고, 적절한 데이터 처리를 도와주는 기술,,,

from fastapi import FastAPI

app = FastAPI()
@app.get('/items/{item_id}')
def read_item(item_id: int): # 경로 매개변수의 type를 int로 지정
    return {'item_id' : item_id}

@app.get('/getdata/')
def read_items(data:str='fast api type hint'): # 쿼리 매개변수의 type은 str, 애개변수값이 입력되지 않으면 기본값을 사용...
    return {'data' : data}

# 고급 타입 힌트 방식 
from fastapi import Query
from typing import List,Dict

@app.get('/items1/')
async def read_items(q: List[int] = Query([])):
    return {'q' : q}

@app.post('/create-item/')
async def create_item(item: Dict[str, int]):
    return item

# Optional[str] : 문자열 또는 None
# Union[int, str] : 정수 또는 문자