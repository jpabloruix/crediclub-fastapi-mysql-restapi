from fastapi import FastAPI
from routes.credito import credito 

app = FastAPI()

app.include_router(credito)