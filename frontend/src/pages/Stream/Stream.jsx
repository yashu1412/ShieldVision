// import React, { useState } from 'react';
// import { useParams } from 'react-router-dom';
// import SideMenu from '../../components/SideMenu/SideMenu';
// import SignOutButton from '../../components/authentication/LogOutButton/SignOutButton';
// import './Stream.css';

// /**
//  * Stream Page — displays a live camera feed in a full-width player.
//  */
// const Stream = () => {
//   const { camera } = useParams();
//   const cameraUrl = decodeURIComponent(camera || '');
//   const [error, setError] = useState(false);

//   const handleError = () => {
//     setError(true);
//     console.error('Error loading stream. Check stream URL or server status.');
//   };

//   return (
//     <div id="streamPage">
//       <SideMenu />
//       <SignOutButton />

//       <div className="playerContainer glass-strong fade-in">
//         {error ? (
//           <div className="errorMessage">
//             <p>⚠️ Unable to load stream. Please check connection or refresh.</p>
//           </div>
//         ) : (
//           <img
//             className="streamMedia"
//             src={cameraUrl}
//             alt="Live camera stream"
//             onError={handleError}
//           />
//         )}
//       </div>
//     </div>
//   );
// };

// export default Stream;

//to run this script python d:\dev\shieldvision\frontend\src\pages\Stream\Stream.py - python Stream.py
 import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import SideMenu from '../../components/SideMenu/SideMenu';
import SignOutButton from '../../components/authentication/LogOutButton/SignOutButton';
import './Stream.css';

/**
 * Stream Page — displays a live camera feed in a full-width player with object detection.
 */
const Stream = () => {
  const { camera } = useParams();
  const cameraUrl = decodeURIComponent(camera || '');
  const [error, setError] = useState(false);
  const [streamUrl, setStreamUrl] = useState('');

  useEffect(() => {
    // Connect to the Python Flask server's video feed endpoint
    if (cameraUrl) {
      // Use the Flask server's video_feed endpoint with the camera URL as a parameter
      setStreamUrl(`http://localhost:7000/video_feed?cameraUrl=${encodeURIComponent(cameraUrl)}`);
    }
  }, [cameraUrl]);

  const handleError = () => {
    setError(true);
    console.error('Error loading stream. Check stream URL or server status.');
  };

  return (
    <div id="streamPage">
      <SideMenu />
      <SignOutButton />

      <div className="playerContainer glass-strong fade-in">
        {error ? (
          <div className="errorMessage">
            <p>⚠️ Unable to load stream. Please check connection or refresh.</p>
            <p>Make sure the Python server is running at localhost:7000</p>
          </div>
        ) : streamUrl ? (
          <img
            className="streamMedia"
            src={streamUrl}
            alt="Live camera stream with object detection"
            onError={handleError}
          />
        ) : (
          <div className="loadingMessage">
            <p>Loading stream...</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Stream;
