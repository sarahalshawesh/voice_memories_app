from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.upload import router as upload_router
from app.routes.get import router as get_recordings_router 
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.config import UPLOAD_DIR


app = FastAPI()

origins = [
    "http://localhost", 
    "http://localhost:3000", 
    "http://127.0.0.1:3000", 
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "https://blether.vercel.app"
]
app.add_middleware(CORSMiddleware, allow_origins = origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")

app.include_router(upload_router)
app.include_router(get_recordings_router)



