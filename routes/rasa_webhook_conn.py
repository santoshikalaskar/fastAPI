from fastapi import APIRouter, HTTPException, status
import requests
from models.end_user import end_User 
from typing import Union
from config.database import db 
import json
from schemas.user import serializeList, serializeDict, userEntity
from bson.objectid import ObjectId


rasa_conn = APIRouter() 

def chat_rasa_bot(message, user_object_id):

    # check user id is valid or not 
    find_user = db.end_User.find_one({"_id": ObjectId(user_object_id)})
    if find_user['email']:
        print("Valid User...!")

        payload = json.dumps({"sender": find_user['email'],"message": message})

        headers = {'Content-type': 'application/json', 'Accept':'text/plain'}

        # hit the URL
        response = requests.post(url="http://localhost:5005/webhooks/rest/webhook", headers=headers, data=payload)

        response = response.json()
        return {"data": response, "User Id": find_user['email'], "Object Id": user_object_id}

@rasa_conn.post('/bl_bot', status_code=status.HTTP_200_OK)
async def chat_to_bL_bot(message: Union[str, None] = None, user_object_id: Union[str, None] = None):
    return chat_rasa_bot(message, user_object_id)
