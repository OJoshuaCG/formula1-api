from fastapi import FastAPI
from routers import races#, drivers

app = FastAPI()

app.include_router(races.router)
# app.include_router(drivers.router)

@app.get("/")
async def root():
    return {"message": "¡Hola desde FastAPI!"}