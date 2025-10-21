import React, { useEffect, useState } from 'react';
import './AccountInfo.css';
import ai from '../../img/ai.png';
import { getUser, getUserObject } from '../../managers/authManager';
import { logError } from '../../utils/logger';

const AccountInfo = ({ style }) => {
  // State to store user information
  const [user, setUser] = useState({
    firstName: "",
    email: "",
    cameras: [],
    maxCameras: 0
  });

  useEffect(() => {
    // Function to fetch user information and update state
    const fetchUser = async () => {
      try {
        // Get user object
        const user = await getUserObject();

        // Default max cameras no longer depends on subscription
        user.maxCameras = user.cameras?.length ?? 0;
        setUser(user);
      } catch (error) {
        logError(error.message);
      }
    };

    // Fetch user information when the component mounts
    fetchUser();
  }, []);

  return (
    <div className={"item2 " + style}>
      <div className='imageContainer'>
        {/* User profile image */}
        <img id='profileImg' src={ai} alt="" />
        <h2 id='profileTitle'>Hello {user.firstName}! 👋</h2>
        <p className='accountInfoLine'>{user.email}</p>
      </div>
      <div className='accountInfoContainer'>
        {/* User account information */}
        <p className='accountInfoLine'><strong>Cameras:</strong> {user.cameras.length}</p>
        <p className='accountInfoLine'><strong>Max Cameras:</strong> {user.maxCameras}</p>
      </div>
    </div>
  );
}

export default AccountInfo;
