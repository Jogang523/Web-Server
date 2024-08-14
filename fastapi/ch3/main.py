# Pydantic 모델
# pydantic 데이터 유효성 검사, 직렬화, 역직렬화를 위해 사용되는 클래스
# 함수의 요청 및 응답 데이터의 타입을 명시하는데 사용
# 데이터에 대한 추가적인 검증 로직을 적게 작성하면서, 타입의 안정성과 깔끔한 유지보수가 가능하도록 한다.

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Union

app = FastAPI()


class Item0(BaseModel): #pydantic 모델을 class로 정의
    name: str
    price: float
    is_offer: bool = None

class Item1(BaseModel):
    name : str
    description : Optional[str]=None
    price : float
    tax : float = 0.1

class Item2(BaseModel):
    name : str = Field(..., title="item Name", min_lenth=2, max_length=50) # ...: 필수 입력 변수
    description : str = Field(None, description ="description of item", max_length=300)
    price : float = Field(..., gt=0, description='greater than zero')
    tag : List[str] = Field(default=[], alias='item-tags')

# 중접된 pydantic model
class Image(BaseModel):
    url : str
    name : str

class Item3(BaseModel):
    name: str
    description : str
    image : Image

class Item4(BaseModel):
    name : str
    tags : List[str]
    variant : Union[int, str]

@app.post("/items/")
def create_item(item : Item0):
    return {"item" : item.dict()}

@app.post("/items1/")
async def create_item(item : Item1):
    return {"item" : item.dict()} 

@app.post("/items2/")
async def create_item(item : Item2):
    return {"item" : item.dict()} 

@app.post("/items3/")
async def create_item(item : Item3):
    return {"item" : item.dict()} 

@app.post("/items4/")
async def create_item(item : Item4):
    return {"item" : item.dict()} 

