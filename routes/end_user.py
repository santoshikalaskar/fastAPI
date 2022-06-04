from fastapi import APIRouter, HTTPException, status
from models.end_user import end_User 
from config.database import db 
from schemas.user import serializeList, serializeDict, userEntity


end_user = APIRouter() 

@end_user.get('/')
def welcome():
    return {"detail":"Welcome to Bridgelabz Chatbot program..!!!"}


@end_user.get('/end_user', status_code=status.HTTP_200_OK)
async def find_all_users():
    
    data = serializeList(db.end_User.find())
    
    if not data:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="End Users data not Available!!!")
    
    return serializeList(db.end_User.find())


@end_user.post('/end_user', status_code=status.HTTP_200_OK)
async def create_new_user(user: end_User):
        existing_user = db.end_User.find_one({"email": user.email})
        if existing_user is not None:
            raise HTTPException(status_code=404, 
                                detail= {"data": f"User with {user.email} is already Exist",
                                        "Object Id": str(existing_user["_id"])})
        new_user = db.end_User.insert_one(dict(user))
        
        if not new_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid input data!!!")
        
        created_user = db.end_User.find_one({"_id": new_user.inserted_id})
        
        return {"data": f"New User with {created_user['email']} is created Successfully...!!!",
            "Object Id": str(created_user["_id"])}
