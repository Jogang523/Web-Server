# response 형식을 지정
# response_model의
# 1. 데이터 검증 : 리턴 값에 대해 지정된 형식에 맞는지 유효성 검증을 자동으로 처리해줌
# 2. 자동문서 생성: 응답형식에 대한 api문서 생성
# 3. 보안 강화 : 노출되지 않아야 할 정도를 숨길 수 있다.

from fastapi import FastAPI
from typing import Optional, List, Dict, Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel): #pydantic model => 객체 dictionary
    name : str
    description : str = None
    price : float

def get_item_from_db(id):
    return{
        "name":"simple item",
        "description" : "simple item description",
        "price" : 5,
        "dis_price" : 45.0
    }

@app.get("/items/{item_id}", response_model = Item)
def read_item(item_id : int):
    item = get_item_from_db(item_id) # return값의 형식을 지정
    return item

# Union 응답 모델

class Cat(BaseModel):
    name : str

class Dog(BaseModel):
    name : str

@app.get("/animal/", response_model=Union[Cat,Dog])
async def get_animal(animal : str):
    if animal == 'cat':
        return Cat(name = "whisker") # Cat pydantic
    else:
        return Dog(name="fido")

# List 응답 모델

class Item(BaseModel):
    name : str

@app.get("/item/", response_model=List[Item])
async def get_item():
    return [{'name':'item1'},{'name':'item2'}] 