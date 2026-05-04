import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

UPLOAD_DIR = Path(__file__).resolve().parents[1] / "uploads"
APP_ENV = os.getenv("APP_ENV", "dev")
STORAGE_BACKEND = os.getenv("STORAGE_BACKEND", "local")
DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")