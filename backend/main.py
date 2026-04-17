from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/upload")
async def save_recording():
    return {"message": "Recording saved"}