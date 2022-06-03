from fastapi import APIRouter, HTTPException, status
from typing import Union
from models.end_user import end_User 
from config.database import db 
from schemas.user import serializeList, serializeDict

get_question = APIRouter() 

@get_question.post('/user_question', status_code=status.HTTP_200_OK)
async def user_question(question: Union[str, None] = None):
    item = {"question": question}
    return item
