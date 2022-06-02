from pydantic import BaseModel, EmailStr
from typing import Union

class end_User(BaseModel):
    name: Union[str, None] = None 
    email : EmailStr
    mobile_number: Union[int, None] = None
   
   