import os

class Config:

    host = os.environ["dbhost"]
    port = os.environ["dbport"]
    username = os.environ["chatbotuser"]
    password = os.environ["chatbotpass"]
    database_name = os.environ["database"]
       
        
       

   