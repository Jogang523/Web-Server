from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id : int):
    try:
        if item_id < 0:
            raise ValueError("음수는 허용되지 않습니다")
        return 100/item_id
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))