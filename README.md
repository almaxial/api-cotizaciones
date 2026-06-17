# Mi API de cotizaciones

API REST en FastAPI que consume una API pública de cotizaciones,
procesa la respuesta y la expone como JSON.

## Qué demuestra
- FastAPI + async/await + httpx (consumo de APIs externas)
- Validación con Pydantic, manejo de errores con status codes
- Tests con pytest, proyecto estructurado en routers

## Cómo correrlo
```
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
fastapi dev app/main.py
```
Después: http://127.0.0.1:8000/docs

## Endpoints
- `GET /dolar/{tipo}` — cotización (oficial, blue, tarjeta…)