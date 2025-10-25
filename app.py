from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(title="My FastAPI Application", version="1.0.0")

# In-memory data storage
data = [{"name": "Sam Larry", "Age": 20, "track": "AI Developer"},
        {"name": "John Doe", "Age": 21, "track": "Backend Developer"},
        {"name": "Jane Smith", "Age": 22, "track": "Frontend Developer"}]


# Pydantic model for request body

class Item(BaseModel):
    name: str = Field(..., example="Alice Johnson")
    age: int = Field(..., example=30)
    track: str = Field(..., example="Data Scientist")


# API Endpoints
@app.get("/", description="This endpoint returns a welcome message.")
def root():
    return {"message": "Welcome to My FastAPI Application"}


# GET all data
@app.get("/get-data")
def get_data():
    """
    To get all data entries
    """
    return {"data": data}

# GET data by ID
# @app.get("/get-data/{id}")
# def get_data_by_id(id: int):
#     """
#     To get data by ID
#     """
#     return {"data": data[id]}


# POST new data
@app.post("/create-data")
def create_data(req: Item):
    data.append(req.dict())
    print(data)
    return {"Message": "Data Received", "data": data}


# PUT to update data
@app.put("/update-data/{id}")
def update_data(id: int, req: Item):
    data[id] = req.dict()
    print(data)
    return {"Message": "Data Updated", "Data": data}

# Write an endpoint to patch and delete entries from the data var.

# Patch data
@app.patch("/patch-data/{id}")
def patch_data(id: int, req: Item):
    stored_data = data[id]
    update_data = req.dict(exclude_unset=True)
    stored_data.update(update_data)
    data[id] = stored_data
    print(data)
    return {"Message": "Data Patched", "Data": data}


# Delete data
@app.delete("/delete-data/{id}")
def delete_data(id: int):
    data.pop(id)
    print(data)
    return {"Message": "Data Deleted", "Data": data}

if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))