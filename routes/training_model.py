from io import BytesIO
from fastapi import APIRouter, HTTPException, status, File, UploadFile
import pandas as pd
from typing import Union
from config.database import db 


training_model = APIRouter() 

@training_model.post('/read_training_csv', status_code=status.HTTP_200_OK)
async def read_training_csv(csv_file: UploadFile = File(...)):
    contents = await csv_file.read()
    buffer = BytesIO(contents)
    df = pd.read_csv(buffer)
    print(df.head())
    return {"df ": "success!"}


