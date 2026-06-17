# app/main.py
from fastapi import FastAPI
from app.routers import dolar

app = FastAPI(title="Mi API de cotizaciones")

app.include_router(dolar.router)

@app.get("/")
async def raiz():
    return {"mensaje": "API funcionando"}