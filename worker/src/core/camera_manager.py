import threading
from src.config.logger import logger
from src.core.stream_processor import process_stream

class CameraManager:
    def __init__(self):
        self.cameras = {}

    def start_camera(self, camera_id, rtsp_url):
        if camera_id in self.cameras:
            return f"Camera {camera_id} already running"
        thread = threading.Thread(target=process_stream, args=(camera_id, rtsp_url), daemon=True)
        self.cameras[camera_id] = thread
        thread.start()
        logger.info(f"[{camera_id}] Stream started")
        return f"Camera {camera_id} started"

    def stop_camera(self, camera_id):
        # Simplified: in a real worker, signal thread stop
        if camera_id not in self.cameras:
            return f"Camera {camera_id} not found"
        del self.cameras[camera_id]
        logger.info(f"[{camera_id}] Stream stopped")
        return f"Camera {camera_id} stopped"

manager = CameraManager()
