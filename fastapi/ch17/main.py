from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import uvicorn
from io import BytesIO
from PIL import Image
import base64

app=FastAPI()

model = load_model("dog_breed.h5")
class_names = ['Scottish Deerhound', 'Maltese Dog', 'Bernese Mountain Dog']

html_template= """
<!DOCTYPE html>
<html>
<head>
    <title>Dog breed Prediction</title>
</head>

<body>
    <h1>Dog breed Prediction</h1>
    <h3>Upload an image of the dog</h3>

    <form action = '/predict' enctype = 'multipart/form-data' method='post'>
        <input name='file' type='file'>
        <input type='submit' value='predict'>
    </form>
    <br><br>
    {image_tag}
    {prediction}
</body>
</html>
"""

@app.get('/', response_class=HTMLResponse)
def home():
    return HTMLResponse(content=html_template.format(image_tag="",prediction=""),status_code=200)

@app.post("/predict",response_class=HTMLResponse)
async def prediction(file: UploadFile=File(...)):

    if file.content_type not in ['image/jpeg','image/png']:
        raise HTTPException(status_code=400, detail='invalid file type..')
    
    contents = await file.read()
    image = Image.open(BytesIO(contents))

    opencv_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    opencv_img = cv2.resize(opencv_img,(224,224))

    opencv_img = np.expand_dims(opencv_img, axis=0)

    y_pred = model.predict(opencv_img)
    predict_class = class_names[np.argmax(y_pred)]

    _, buffer = cv2.imencode(".png", cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR))
    img_str = base64.b64encode(buffer).decode('utf-8')
    image_tag = f'<img src="data:image/pmg;base64,{img_str}" alt="dog image" width="300">'
    prediction= f'<h2> the dog breed is : {predict_class} </h2>'

    return HTMLResponse(content=html_template.format(image_tag=image_tag, prediction=prediction),status_code=200)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)