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

templates=Jinja2Templates(directory='templates')

app = FastAPI()
app.mount("/static", StaticFiles(directory='static'), name='static')

class Car(BaseModel):
    make : Optional[str]
    model : Optional[str]
    year : Optional[int] = Field(..., ge = 1970, lt = 2022)
    price : Optional[float]
    engine : Optional[str] = "V4"
    autonomous : Optional[bool]
    sold : Optional[List[str]]


@app.get("/", response_class=RedirectResponse)
def root(request: Request):
    return RedirectResponse(url='/cars')

@app.get("/cars", response_class=HTMLResponse)
def get_cars(request: Request, number: Optional[str] = Query("10", max_length=3)):
    response = []
    for id, car in list(cars.items())[:int(number)]:
        response.append((id, car))
    return templates.TemplateResponse("index.html", {"request":request, "cars":response, "title":"home"})

@app.post("/search", response_class=RedirectResponse)
def search_cars(id: str = Form(...)):
    return RedirectResponse("/cars/"+id ,status_code=302)

@app.get("/cars/{id}", response_class=HTMLResponse)
def get_car_by_id(request: Request, id : int = Path(..., ge=0, lt=1000)):
    car = cars.get(id)
    response = templates.TemplateResponse("search.html", {"request":request, 'car':car, 'id':id, 'title':'Search home'})
    if not car:
        response.status_code = status.HTTP_404_NOT_FOUND
    return response

@app.get("/create", response_class= HTMLResponse)
def create_car(request:Request):
    return templates.TemplateResponse("create.html",{'request':request,'title':'create_car'})

@app.post("/cars", status_code=status.HTTP_201_CREATED)
def add_cars(
    make: Optional[str] = Form(...),
    model: Optional[str] = Form(...),
    year: Optional[str] = Form(...),
    price: Optional[str] = Form(...),
    engine: Optional[str] = Form(...),
    autonomous: Optional[bool] = Form(...),
    sold: Optional[str] = Form(None)
):
    try:
        year = int(year) if year is not None else None
    except:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,detail="year must be an int")

    if sold is not None:
        sold = [sold] if isinstance(sold, str) else sold

    body_cars = [Car(make=make, 
                    model=model,
                    year=year,
                    price=price,
                    engine=engine,
                    autonomous=autonomous,
                    sold=sold)]
    
    if len(body_cars) < 1:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="no cars to add")
    
    min_id = len (cars) + 1
    for car in body_cars:
        while cars.get(min_id):
            min_id += 1
        cars[min_id] = jsonable_encoder(car)
        min_id += 1

    return RedirectResponse(url="/cars",status_code=302)