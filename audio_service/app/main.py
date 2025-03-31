from fastapi import FastAPI
from audio_service.app.api.api_router import api_router


# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

app = FastAPI(title="Audio Service API")

app.include_router(api_router)
