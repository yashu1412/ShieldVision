from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
import cv2
import threading
import time
import os

app = Flask(__name__)
# Enable CORS for all routes and origins
CORS(app, resources={r"/*": {"origins": "*"}})

# Load YOLO model - use absolute path or check if file exists
model_path = "yolov8n.pt"
if not os.path.exists(model_path):
    print(f"Warning: Model file {model_path} not found. Please download it or provide the correct path.")
    print("Attempting to download model...")

# Load YOLO model
try:
    model = YOLO(model_path)
    print("YOLO model loaded successfully")
except Exception as e:
    print(f"Error loading YOLO model: {e}")
    print("Will run without object detection if model can't be loaded")
    model = None

# Store running capture threads
streams = {}

def generate_frames(camera_url):
    print(f"Attempting to connect to camera: {camera_url}")
    cap = cv2.VideoCapture(camera_url)
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open camera {camera_url}")
        # Yield an error frame
        error_frame = create_error_frame(f"Could not connect to: {camera_url}")
        ret, buffer = cv2.imencode(".jpg", error_frame)
        error_bytes = buffer.tobytes()
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + error_bytes + b"\r\n")
        return
    
    print(f"Successfully connected to camera: {camera_url}")
    
    # Set a timeout for frame reading
    frame_count = 0
    last_log_time = time.time()
    
    while True:
        success, frame = cap.read()
        
        # Log performance every 100 frames
        frame_count += 1
        if frame_count % 100 == 0:
            current_time = time.time()
            elapsed = current_time - last_log_time
            fps = 100 / elapsed if elapsed > 0 else 0
            print(f"Processing at {fps:.2f} FPS")
            last_log_time = current_time
        
        if not success:
            print(f"Failed to read frame from {camera_url}")
            # Create an error frame
            error_frame = create_error_frame("Connection lost")
            ret, buffer = cv2.imencode(".jpg", error_frame)
            error_bytes = buffer.tobytes()
            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + error_bytes + b"\r\n")
            # Try to reconnect
            time.sleep(1)
            cap = cv2.VideoCapture(camera_url)
            continue

        # Run YOLO detection if model is available
        if model is not None:
            try:
                results = model(frame, verbose=False)[0]
                
                # Draw bounding boxes and labels
                for box in results.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    label = model.names[int(box.cls)]
                    conf = float(box.conf)
                    text = f"{label} {conf:.2f}"

                    # Draw rectangle + label
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cv2.putText(frame, text, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            except Exception as e:
                print(f"Error in object detection: {e}")
                # Add error text to frame
                cv2.putText(frame, "Detection error", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Add timestamp to frame
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, timestamp, (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Encode frame as JPEG
        ret, buffer = cv2.imencode(".jpg", frame)
        frame_bytes = buffer.tobytes()

        # Send frame as stream
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n")

    cap.release()

def create_error_frame(message):
    """Create a black frame with error message"""
    frame = np.zeros((480, 640, 3), np.uint8)
    cv2.putText(frame, message, (50, 240),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return frame

@app.route("/video_feed")
def video_feed():
    camera_url = request.args.get("cameraUrl")
    if not camera_url:
        return "Missing camera URL", 400
    
    print(f"Received request for camera: {camera_url}")
    
    # Set response headers for streaming
    return Response(generate_frames(camera_url),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/health")
def health_check():
    """Simple health check endpoint"""
    return jsonify({"status": "ok", "message": "Server is running"})

# Import numpy for error frame creation
import numpy as np

if __name__ == "__main__":
    print("Starting ShieldVision Stream Server on port 7000...")
    app.run(host="0.0.0.0", port=7000, threaded=True)
