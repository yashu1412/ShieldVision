# ShieldVision - RTSP Livestream with Custom Overlays
Live Link :  https://shield-vision.vercel.app/cameras

ShieldVision is a full-stack web application that allows users to view livestream videos from RTSP URLs with the ability to add, manage, and customize overlays. The application provides a user-friendly interface for monitoring camera feeds and offers features like object detection, custom overlays, and user account management.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Playing Livestreams](#playing-livestreams)
  - [Managing Overlays](#managing-overlays)
- [API Documentation](#api-documentation)
- [Testing the Payment System](#testing-the-payment-system)
- [Testing the Surveillance System](#testing-the-surveillance-system)
- [Future Changes](#future-changes)

---

## Features

- **RTSP Livestream Playback**: View livestream videos from any RTSP URL source with basic playback controls (play, pause, volume).
- **Custom Overlays**: Add, position, and resize custom overlays such as logos and text on top of the livestream.
- **Object Detection**: AI-powered object detection using YOLOv8 to identify and highlight objects in the video stream.
- **CRUD Operations for Overlays**: Create, read, update, and delete custom overlay settings through a RESTful API.
- **User Authentication**: Secure user authentication and authorization system to ensure that only authorized users can access the dashboard.
- **Responsive Design**: Designed to be responsive and accessible on desktops, tablets, and mobile phones.

---

## Tech Stack

- **Backend**: Node.js (Express) for handling REST APIs, authentication, and server-side logic.  
- **Frontend**: React.js for building a modern, responsive, and dynamic user interface.  
- **Database**: MongoDB for storing user accounts, camera details, and overlay configurations.  
- **Video Processing**: OpenCV and YOLOv8 for real-time video analysis, object detection, and frame processing.  
- **Authentication**: JWT (JSON Web Token) based system for secure user login and API access.  
- **Worker Service**: Python (Flask) microservice responsible for processing and relaying RTSP streams into MJPEG format for frontend playback.  
- **Containerization**: Docker is used to containerize the Python worker service, enabling consistent and isolated deployment across environments.  


---

## Getting Started

Follow these instructions to set up and run ShieldVision locally on your development machine.

### Prerequisites

Before you begin, make sure you have the following installed:

- [Node.js](https://nodejs.org/)
- [Python 3.8+](https://www.python.org/)
- [MongoDB](https://www.mongodb.com/)
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)

---

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/shieldvision.git
   cd shieldvision
Set up the backend

bash
Copy code
npm install
Set up the frontend

bash
Copy code
cd frontend
npm install --legacy-peer-deps
cd ..
Configure MongoDB

Ensure MongoDB is running locally or update the connection string in the .env file

Default: mongodb://localhost:27017/shieldvision

Start the application

bash
Copy code
# Start backend
npm start

# Start worker (in a new terminal)
cd worker
docker build -t shieldvision-worker:latest .
docker run -p 7000:7000 shieldvision-worker:latest

# Start frontend (in another terminal)
cd frontend
npm start
Access the app
Open http://localhost:3000 in your browser.

Usage
Playing Livestreams
Add an RTSP Stream

Go to the Cameras page

Click Add Camera

Enter a name and RTSP URL (e.g., rtsp://example.com/stream)

Click Save

View a Stream

Click on a camera in your dashboard

Stream loads with object detection enabled

Use controls to play, pause, or adjust volume

Example RTSP URLs

rtsp://demo:demo@ipvmdemo.dyndns.org:5541/onvif-media/media.amp

Managing Overlays
Create an Overlay

Click Add Overlay

Choose type (text/image), position, and resize

Click Save

Edit Overlays

Select an overlay

Modify position, size, or content

Click Update

Delete Overlays

Select the overlay

Click Delete

API Documentation
Authentication
Method	Endpoint	Description
POST	/api/auth/register	Register a new user
POST	/api/auth/login	Login and get a JWT token

Cameras
Method	Endpoint	Description
GET	/api/cameras	Get all user cameras
POST	/api/cameras	Add a new camera
PUT	/api/cameras/:id	Update camera details
DELETE	/api/cameras/:id	Delete a camera

Overlays
Method	Endpoint	Description
GET	/api/overlays	Get overlays for a camera
POST	/api/overlays	Create a new overlay
PUT	/api/overlays/:id	Update overlay
DELETE	/api/overlays/:id	Delete overlay

Streams
Method	Endpoint	Description
GET	/video_feed?cameraUrl=<rtsp_url>	Stream video with object detection


