from fastapi import FastAPI
import pandas as pd

#Create API Object
app = FastAPI()

#Read Data
data = pd.read_csv('data.csv')

# Coba root home API (get)
@app.get("/")
def root():
    return {'message': 'Hello HCK-025'}

# endpoint sapaan
@app.get("/name/{name}")
def greet(name):
    return {'message': f'Hai {name}, how are you?'}

#Endpoint return data
@app.get("/data")
def get_data(): 
    return data.to_dict(orient='records')

#Get data by ID
@app.get("/data/{id}")
def search_data(id:int):
    result = data[data['id'] == id]
    return{'result': result.to_dict(orient='records')}

#Menambahkan data
@app.post("/data/add")
def add_data(new_data:dict):
    global data
    
    new_row = pd.DataFrame([new_data])
    data = pd.concat([data, new_row], ignore_index=True)

    return {'message':data.to_dict(orient='records')}