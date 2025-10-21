

import cv2, time, threading
from src.core.face_detector import FaceDetector
from src.core.object_detector import ObjectDetector
from src.utils.alert_poster import post_alert
from src.config.logger import logger
from src.config.env import MEDIAMTX_URL
from src.utils.minio_uploader import upload_snapshot
import ffmpeg
import numpy as np

def process_stream(camera_id, rtsp_url):
    face_detector = FaceDetector()
    object_detector = ObjectDetector()
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        logger.error(f"[{camera_id}] Unable to open RTSP stream")
        return

    # Setup FFmpeg process for MediaMTX streaming if enabled
    ffmpeg_process = None
    if MEDIAMTX_URL:
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        fps = cap.get(cv2.CAP_PROP_FPS) or 10
        ffmpeg_process = (
            ffmpeg
            .input('pipe:', format='rawvideo', pix_fmt='bgr24', s=f'{width}x{height}', framerate=fps)
            .output(MEDIAMTX_URL, vcodec='libx264', pix_fmt='yuv420p', preset='veryfast', tune='zerolatency', f='rtsp')
            .overwrite_output()
            .run_async(pipe_stdin=True)
        )

    last_snapshot_time = 0
    snapshot_interval = 10  # seconds between MinIO uploads

    while True:
        ret, frame = cap.read()
        if not ret:
            logger.warning(f"[{camera_id}] Failed to grab frame, retrying...")
            time.sleep(2)
            continue

        # Face detection
        faces = face_detector.detect(frame)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Human/animal detection
        objects = object_detector.detect(frame)
        for obj in objects:
            label = obj['label']
            (startX, startY, endX, endY) = obj['box']
            color = (0, 255, 0) if label == 'person' else (255, 0, 0)
            cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
            cv2.putText(frame, f"{label} {obj['confidence']:.2f}", (startX, startY-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Alert logic: send alert if faces or objects detected
        if len(faces) > 0 or len(objects) > 0:
            alert_data = {
                'faces': len(faces),
                'objects': [{ 'label': o['label'], 'confidence': o['confidence'] } for o in objects]
            }
            post_alert(camera_id, alert_data)
            logger.info(f"[{camera_id}] Faces: {len(faces)}, Objects: {alert_data['objects']}")
            # Upload snapshot to MinIO (rate-limited)
            now = time.time()
            if now - last_snapshot_time > snapshot_interval:
                try:
                    url = upload_snapshot(camera_id, frame)
                    logger.info(f"[{camera_id}] Snapshot uploaded to MinIO: {url}")
                except Exception as e:
                    logger.error(f"[{camera_id}] MinIO upload failed: {e}")
                last_snapshot_time = now

        # Stream processed frame to MediaMTX if enabled
        if ffmpeg_process:
            try:
                ffmpeg_process.stdin.write(
                    frame.astype(np.uint8).tobytes()
                )
            except Exception as e:
                logger.error(f"[{camera_id}] MediaMTX streaming error: {e}")

        time.sleep(0.1)

    cap.release()
    if ffmpeg_process:
        ffmpeg_process.stdin.close()
        ffmpeg_process.wait()
