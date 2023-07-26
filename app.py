from fastapi import FastAPI

app = FastAPI()



#an API endpoint 
@app.get("/")
def Hello():
    return {"Hello": "World"}