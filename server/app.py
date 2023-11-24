from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("localhost", 27017)
db = client.test_database
collection = db.test_collection


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add/{my_fruit}")
async def get_fruits(my_fruit: str):
    return {"fruit": str(collection.insert_one({"fruit": my_fruit}).inserted_id)}

@app.get("/list")
async def list_fruits():
    return {"list": list(collection.find({}, {"_id": False}))}