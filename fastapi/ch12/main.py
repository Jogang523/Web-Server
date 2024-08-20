from fastapi import FastAPI, File, UploadFile
import shutil
from pathlib import Path

app = FastAPI()

@app.post('/uploadfile/')
async def create_upload_file(file: UploadFile = File(...)):
    folder_name='uploaded_files'
    Path(folder_name).mkdir(exist_ok=True)
    file_location=f"{folder_name}/{file.filename}"

    file.file.seek(0) # 파일의 첫부분 시작 위치

    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    
    return {"uploaded filename" : file.filename}

#pip install python_multipart==0.0.9