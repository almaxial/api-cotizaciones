# app/routers/dolar.py
from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter(prefix="/dolar", tags=["dolar"])

@router.get("/{tipo}")
async def dolar(tipo: str):
    
    url = f"https://dolarapi.com/v1/dolares/{tipo}"
    try:

        async with httpx.AsyncClient() as client:
             r = await client.get(url)
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail="La API externa no responde")

    if r.status_code == 404:
        raise HTTPException(status_code=404, detail=f"No existe el tipo '{tipo}'")
    
        
        
    datos = r.json()

    print(url)
    print(r.status_code)
    print(r.text) 
    # procesamos: nos quedamos solo con lo que nos importa
    return {
        "moneda": tipo,
        "compra": datos["compra"],
        "venta": datos["venta"],
        "spread": datos["venta"] - datos["compra"],
    }

