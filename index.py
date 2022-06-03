from doctest import debug
from fastapi import FastAPI
from routes.end_user import end_user 
from routes.end_user_question import get_question
from routes.training_model import training_model

app = FastAPI(debug=True)
app.include_router(end_user)
app.include_router(get_question)
app.include_router(training_model)