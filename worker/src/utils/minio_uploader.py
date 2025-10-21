import os
from minio import Minio
from minio.error import S3Error
from datetime import datetime

MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY')
MINIO_BUCKET = os.getenv('MINIO_BUCKET', 'snapshots')

client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

def upload_snapshot(camera_id, frame):
    """Uploads a frame (numpy array) to MinIO and returns the public URL."""
    import cv2
    import io
    # Encode frame as JPEG
    _, buffer = cv2.imencode('.jpg', frame)
    data = io.BytesIO(buffer)
    # Generate object name
    now = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    object_name = f"{camera_id}/{now}.jpg"
    # Ensure bucket exists
    if not client.bucket_exists(MINIO_BUCKET):
        client.make_bucket(MINIO_BUCKET)
    # Upload
    client.put_object(
        MINIO_BUCKET,
        object_name,
        data,
        length=data.getbuffer().nbytes,
        content_type='image/jpeg'
    )
    url = f"http://{MINIO_ENDPOINT}/{MINIO_BUCKET}/{object_name}"
    return url
