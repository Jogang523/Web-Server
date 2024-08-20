import asyncio

async def func1():
    print("func1 : start")
    await asyncio.sleep(3)
    print("func1 : End")
    return {"data" : "some_data"}

async def func2():
    print("func2 : start")
    await asyncio.sleep(1)
    print("func2 : End")
    return {"data" : "some_data"}


async def main():
    await asyncio.gather(func1(),func2()) # asyncio.gather() : 여러 비동기 함수를 한번에 실행


if __name__ == "__main__":
    asyncio.run(main()) # asyncio.run(비동기 함수) : 비동기 함수를 실행시키는 명령