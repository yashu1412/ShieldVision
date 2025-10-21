/**
 * API Configuration
 * This file contains the configuration for the backend API
 */

// Backend base URL
export const API_BASE_URL = 'https://shieldvision-1.onrender.com/';

// API endpoints
export const API_ENDPOINTS = {
  // Authentication
  REGISTER: `${API_BASE_URL}/api/register`,
  LOGIN: `${API_BASE_URL}/api/authentication/login`,
  GET_USER: `${API_BASE_URL}/api/authentication/get-user`,
  UPDATE_USER: `${API_BASE_URL}/api/authentication/update-user`,
  GET_ALL_USERS: `${API_BASE_URL}/api/authentication/get-all-users`,
  DELETE_USER: `${API_BASE_URL}/api/authentication/test`,
  
  // Cameras
  ADD_CAMERA: `${API_BASE_URL}/api/cameras/add`,
  UPDATE_CAMERA: `${API_BASE_URL}/api/cameras/update`,
  REMOVE_CAMERA: `${API_BASE_URL}/api/cameras/remove`,
  GET_CAMERAS: `${API_BASE_URL}/api/cameras/get-cameras`,
  
  // Stream
  VIDEO_FEED: `${API_BASE_URL}/video_feed`,
};

export default API_ENDPOINTS;