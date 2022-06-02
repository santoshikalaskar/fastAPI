from doctest import debug
from fastapi import FastAPI
from routes.end_user import end_user 

app = FastAPI(debug=True)
app.include_router(end_user)
