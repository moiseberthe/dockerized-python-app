from fastapi import FastAPI
from pymongo import MongoClient
import pandas as pd
import pickle

app = FastAPI()

client = MongoClient("mongo", 27017)
db = client.test_database
collection = db.test_collection

# load iris model
with open("decision-tree.pkl", "rb") as f:
    data = pickle.load(f)

# load penguins model
with open("penguins-decision-tree.pkl", "rb") as f:
    model_p = pickle.load(f)

p_cols = ['island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']
model_i = data["model"]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add/{my_fruit}")
async def get_fruits(my_fruit: str):
    return {"fruit": str(collection.insert_one({"fruit": my_fruit}).inserted_id)}

@app.get("/list")
async def list_fruits():
    return {"list": list(collection.find({}, {"_id": False}))}

@app.get("/predict/iris/{sepal_length}/{sepal_width}/{petal_length}/{petal_width}")
async def predict(sepal_length,  sepal_width,  petal_length,  petal_width):
    variety = model_i.predict(
        [[sepal_length, sepal_width, petal_length, petal_width]]
    )[0]
    
    return {"prediction": variety}

@app.get("/predict/penguins/{island}/{bill_length_mm}/{bill_depth_mm}/{flipper_length_mm}/{body_mass_g}/{sex}")
async def predict_penguins(island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex):
    specy = model_p.predict(pd.DataFrame([[island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex]], columns=p_cols))[0]
    
    return {"prediction": specy}