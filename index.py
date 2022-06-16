from doctest import debug
from fastapi import FastAPI
from routes.end_user import end_user 
from routes.rasa_webhook_conn import rasa_conn

app = FastAPI(debug=True)

# user route
app.include_router(end_user)

# Rasa webhook route
app.include_router(rasa_conn)

