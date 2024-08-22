from fastapi import FastAPI, Path, HTTPException, status, Body, Request, Form, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from starlette.responses import HTMLResponse
from starlette.status import HTTP_400_BAD_REQUEST
from database import cars

templates = Jinja2Templates(directory='templates')

app = FastAPI()
app.mount("/static", StaticFiles(directory='static'), name='static')

# --- 목록 조회

@app.get("/", response_class=RedirectResponse)
def root(request: Request):
    return RedirectResponse(url='/cars')

@app.get("/cars", response_class=HTMLResponse)
def get_cars(request: Request, number: Optional[str] = Query("10", max_length=3)):
    response = []
    for id, car in list(cars.items())[:int(number)]:
        response.append((id, car))
    return templates.TemplateResponse("index.html", {"request":request, 'cars':response, 'title':'Home'})

# -- search

@app.post("/search", response_class=RedirectResponse)
def search_cars(id: str = Form(...)):
    return RedirectResponse("/cars/"+id, status_code=302)

@app.get("/cars/{id}", response_class=HTMLResponse)
def get_car_by_id(request: Request, id: int = Path(..., ge=0, lt=1000)):
    car = cars.get(id)
    response = templates.TemplateResponse("search.html", {"request":request, 'cars':car, 'title':'Home'})
    if not car:
        response.status_code = status.HTTP_404_NOT_FOUND
        return response