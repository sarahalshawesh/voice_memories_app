from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.upload import router as upload_router

app = FastAPI()

origins = [
    "http://localhost", 
    "http://localhost:3000", 
    "http://127.0.0.1:3000"
]
app.add_middleware(CORSMiddleware, allow_origins = origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(upload_router)

@app.get("/")
async def read_root(): 
    return {"Hello": "World"}

@app.get("/health")
async def health():
    return {"status": "ok"}

