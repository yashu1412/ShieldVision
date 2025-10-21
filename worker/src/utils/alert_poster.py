import requests
from src.config.env import BACKEND_URL, WORKER_SECRET
from src.config.logger import logger

def post_alert(camera_id, alert_data):
    try:
        payload = {"cameraId": camera_id, **alert_data}
        headers = {"Authorization": f"Bearer {WORKER_SECRET}"}
        response = requests.post(f"{BACKEND_URL}/alerts", json=payload, headers=headers, timeout=5)
        logger.info(f"Alert sent for camera {camera_id} [{response.status_code}]")
    except Exception as e:
        logger.error(f"Failed to post alert: {e}")
