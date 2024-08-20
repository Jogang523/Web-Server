import asyncio
from fastapi import FastAPI
from time import sleep, time
import requests
import aiohttp

app = FastAPI()
default_url = "https://www.nate.com"

# 동기방식
@app.get("/sync/{time}")
def sync_call(times : int, url : str = default_url):
    start_time = time()
    sleep(1)
    for _ in range(times):
        requests.get(url)
    elasped_time_sync = time()
    return [ 'elasped_time_sync:', round(elasped_time_sync,3)]

# 비동기식
@app.get("/sync/{times}")
async def async_call(times : int, url : str = default_url):
    start_time = time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(times):
            task = session.get(url)
            tasks.append(task)
        await asyncio.gather(*tasks)
    elasped_time_async = time()
    return [ 'elasped_time_async:', round(elasped_time_async,3)]
