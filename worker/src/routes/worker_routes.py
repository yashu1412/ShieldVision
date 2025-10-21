from flask import Blueprint, request, jsonify
from src.core.camera_manager import manager

bp = Blueprint("worker_routes", __name__)

@bp.route("/start", methods=["POST"])
def start_camera():
    data = request.get_json()
    camera_id = data.get("cameraId")
    rtsp_url = data.get("rtspUrl")
    msg = manager.start_camera(camera_id, rtsp_url)
    return jsonify({"message": msg}), 200

@bp.route("/stop", methods=["POST"])
def stop_camera():
    data = request.get_json()
    camera_id = data.get("cameraId")
    msg = manager.stop_camera(camera_id)
    return jsonify({"message": msg}), 200

@bp.route("/status", methods=["GET"])
def status():
    return jsonify({"activeCameras": list(manager.cameras.keys())})
