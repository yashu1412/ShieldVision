import os
from dotenv import load_dotenv

load_dotenv()

WORKER_SECRET = os.getenv("WORKER_SECRET")
BACKEND_URL = os.getenv("BACKEND_URL")
MAX_STREAMS = int(os.getenv("MAX_STREAMS", 4))
MEDIAMTX_URL = os.getenv("MEDIAMTX_URL")
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_BUCKET = os.getenv("MINIO_BUCKET")
