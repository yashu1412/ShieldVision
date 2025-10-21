import React, { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { loadPlayer } from 'rtsp-relay/browser';
import settingsIcon from '../../img/settings.png';
import './SecurityCamera.css';

/**
 * SecurityCamera component for displaying a security camera stream.
 * @param {string} cameraUrl - The URL of the camera stream.
 * @param {function} setCameraToEdit - Function to set the camera for editing.
 * @param {number} index - The index of the camera.
 * @param {boolean} isPreview - Whether it's a camera preview.
 */
const SecurityCamera = ({ cameraUrl, setCameraToEdit, index, isPreview }) => {
  const navigate = useNavigate();
  // WebSocket stream URL for the camera
  const streamUrl = `ws://localhost:8080/api/stream/${encodeURIComponent(cameraUrl)}`;

  // Reference to the canvas element
  const canvas = useRef(null);
  // Reference to the image element
  const imageRef = useRef(null);

  // Set canvas style after a delay
  const setCanvasStyle = () => {
    setTimeout(() => {
      if (!canvas.current) return;
      canvas.current.width = 320;
      canvas.current.height = 180;
      canvas.current.style.display = index > 0 ? 'flex' : 'none';
    }, 4000);
  };

  useEffect(() => {
    if (!canvas.current) return;

    // Check if the camera URL starts with "http" (static image)
    if (cameraUrl.startsWith("http")) return;

    // Load the RTSP player
    loadPlayer({
      url: streamUrl,
      canvas: canvas.current,
      videoBufferSize: 1024 * 1024,
      onPlay: setCanvasStyle,
      audio: false,
      disableGl: true,
    });
  }, [cameraUrl, streamUrl]);

  return (
    <div className='camera'>
      {/* Show settings icon for non-preview cameras */}
      {!isPreview && (
        <img onClick={() => setCameraToEdit(cameraUrl)} className='deleteIcon' src={settingsIcon} alt="Settings" />
      )}

      {/* Canvas element for displaying the camera stream */}
      <canvas onClick={() => navigate(`/stream/${encodeURIComponent(cameraUrl)}`)} className={index === 0 || cameraUrl.startsWith("http") ? 'hiddenCamera' : 'camera'} ref={canvas} />

      {/* Image element for displaying static images */}
      <img onClick={() => navigate(`/stream/${encodeURIComponent(cameraUrl)}`)} ref={imageRef} src={cameraUrl} className={cameraUrl.startsWith("http") ? "camera" : "hiddenCamera"} alt="Camera" />

      {/* View stream button */}
      {!isPreview && (
        <button onClick={() => navigate(`/stream/${encodeURIComponent(cameraUrl)}`)} className='btn-red' style={{ position: 'absolute', bottom: 8, right: 8 }}>View Stream</button>
      )}
    </div>
  );
}

export default SecurityCamera;
