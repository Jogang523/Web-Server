from fastapi import FastAPI
import asyncio

app = FastAPI()

async def fetch_data(): # 비동기 처리를 위해 함수 앞에 async
    await asyncio.sleep(2) # 함수 내에서 비동기 처리할 부분에 await
    return {"data":"some_data"}

@app.get("/")
async def read_root():
    data = await fetch_data()
    return {"message":"hello world", "fetch_data": data}

# 동기처리
# 프로세스 단위로 하나씩 프로그램 작업을 처리

# 비동기 처리
# 프로세스를 여러 프로세스의 작업을 나누어서 번갈아가면서 처리