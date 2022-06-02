from fastapi import APIRouter
from models.end_user import end_User 
from config.database import db 
from schemas.user import serializeList, serializeDict


end_user = APIRouter() 

@end_user.get('/')
async def find_all_users():
    return serializeList(db.end_User.find())

@end_user.post('/')
async def create_user(user: end_User):
        obj = db.end_User.insert_one(dict(user))
        return serializeDict(db.end_User.find())

