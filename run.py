import uvicorn
from db.database import Database

if __name__ == "__main__":

    Database.init_database()
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)