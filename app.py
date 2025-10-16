from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(title="My FastAPI Application", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Welcome to My FastAPI Application"}


if __name__ == "__main__":
    print(os.getenv("host")), 
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))