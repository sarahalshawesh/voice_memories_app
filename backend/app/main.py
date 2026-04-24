from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.upload import router as upload_router
from backend.app.routes.get import router as get_recordings_router 



app = FastAPI()

origins = [
    "http://localhost", 
    "http://localhost:3000", 
    "http://127.0.0.1:3000"
]
app.add_middleware(CORSMiddleware, allow_origins = origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(upload_router)
app.include_router(get_recordings_router)



