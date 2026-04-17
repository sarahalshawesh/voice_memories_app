from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost", 
    "http://localhost:3000", 
    "http://127.0.0.1:3000"
]
app.add_middleware(CORSMiddleware, allow_origins = origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/")
async def read_root(): 
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/upload")
async def save_recording():
    return {"message": "Recording saved"}