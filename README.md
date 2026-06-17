# API de Cotizaciones

API desarrollada con FastAPI que consulta cotizaciones del dólar desde una API externa.

## Tecnologías

- Python
- FastAPI
- HTTPX
- Pytest
- Git y GitHub

## Funcionalidades

- Consulta cotizaciones por tipo de dólar.
- Consumo de APIs externas.
- Cálculo automático del spread.
- Validación de respuestas.
- Tests automatizados.

## Instalación

```bash
pip install -r requirements.txt

## Ejecución

fastapi dev app/main.py
```
Después: http://127.0.0.1:8000/docs

## Endpoints
- `GET /dolar/{tipo}` — cotización (oficial, blue, tarjeta…)