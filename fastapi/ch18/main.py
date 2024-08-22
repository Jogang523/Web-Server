# pip install fastapi uvicorn opencv-python-headless jinja2

import os
import cv2
import logging as log
import datetime as dt
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from io import BytesIO
import numpy as np

app = FastAPI()

# Set up paths
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)
log.basicConfig(filename='webcam.log', level=log.INFO)

# Set up templates
templates = Jinja2Templates(directory="templates")

# Serve static files (if needed, for CSS/JS)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Video capture variable
video_capture = cv2.VideoCapture(0)
anterior = 0

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Renders the main page with a button to start face detection."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/detect/")
async def detect_faces(file: UploadFile = File(...)):
    """Endpoint to detect faces in an uploaded image."""
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    _, img_encoded = cv2.imencode('.jpg', img)
    return StreamingResponse(BytesIO(img_encoded.tobytes()), media_type="image/jpeg")

@app.get("/video_feed")
async def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return StreamingResponse(generate_video(), media_type="multipart/x-mixed-replace; boundary=frame")

def generate_video():
    global anterior
    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if anterior != len(faces):
            anterior = len(faces)
            log.info("faces: " + str(len(faces)) + " at " + str(dt.datetime.now()))

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# uvicorn main:app --reload