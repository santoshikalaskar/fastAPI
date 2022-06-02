from tokenize import Double
from pydantic import BaseModel, EmailStr, Field
from fastapi import FastAPI, Query
from typing import Union

class end_User(BaseModel):
    name: str = Field( default="your name", title="Enter your Name", max_length=50 )
    email : EmailStr = Field( default="your Email Id", title="Enter your mail ID" )
    mobile_number: int = Field(description="The Mobile number must be 10 digit")
   
   