import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.api import api_router
from db import database

load_dotenv(".env")
app = FastAPI(title="Binance bot")
app.mount("/static", StaticFiles(directory="static"), name="/static")
app.include_router(api_router)


@app.on_event("startup")
async def startup():
    print("inicializando...")
    database.connect()


@app.on_event("shutdown")
async def shutdown():
    print("terminando...")
    database.close()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
