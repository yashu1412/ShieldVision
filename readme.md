# ShieldVision - RTSP Livestream with Custom Overlays

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

## Features

- **RTSP Livestream Playback**: View livestream videos from any RTSP URL source with basic playback controls (play, pause, volume).

- **Custom Overlays**: Add, position, and resize custom overlays such as logos and text on top of the livestream.

- **Object Detection**: AI-powered object detection using YOLOv8 to identify and highlight objects in the video stream.

- **CRUD Operations for Overlays**: Create, read, update, and delete custom overlay settings through a RESTful API.

- **User Authentication**: Secure user authentication and authorization system to ensure that only authorized users can access the dashboard.

- **Responsive Design**: The application is designed to be responsive and accessible on various devices, including desktops, tablets, and mobile phones.

## Tech Stack

- **Backend**: For the server-side application and video processing
- **Frontend**: React.js for the user interface
- **Database**: MongoDB for storing user data and overlay settings
- **Video Processing**: OpenCV and YOLOv8 for video stream handling and object detection
- **Authentication**: JWT-based authentication system

## Getting Started

Follow these instructions to set up and run ShieldVision locally on your development machine.

### Prerequisites

Before you begin, make sure you have the following software installed:

- [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/) (Node Package Manager)
- [Python](https://www.python.org/) (3.8 or higher)
- [MongoDB](https://www.mongodb.com/) (local or Atlas)
- [Git](https://git-scm.com/) (for cloning the project repository)

### Installation

1. **Clone the repository**
   ```
   git clone https://github.com/yourusername/shieldvision.git
   cd shieldvision
   ```

2. **Set up the backend**
   ```
   # Install Node.js dependencies
   npm install
   
   # Install Python dependencies
   pip install flask flask-cors ultralytics opencv-python
   ```

3. **Set up the frontend**
   ```
   cd frontend
   npm install --legacy-peer-deps
   cd ..
   ```

4. **Configure MongoDB**
   - Ensure MongoDB is running locally or update the connection string in `.env` file
   - The default connection is `mongodb://localhost:27017/shieldvision`

5. **Start the application**
   ```
   # Start the backend server
   npm start
   
   # In a separate terminal, start the Python Flask server
   python frontend/src/pages/Stream/Stream.py
   
   # In another terminal, start the React frontend
   cd frontend
   npm start
   ```

6. **Access the application**
   - Open your browser and navigate to `http://localhost:3000/`

## Usage

### Playing Livestreams

1. **Adding an RTSP Stream**
   - Navigate to the Cameras page
   - Click "Add Camera"
   - Enter a name and the RTSP URL (e.g., rtsp://example.com/stream)
   - Click "Save"

2. **Viewing a Stream**
   - Click on any camera from your dashboard
   - The stream will load with object detection enabled
   - Use the playback controls to play, pause, or adjust volume

3. **Testing with Sample RTSP Streams**
   - You can use services like RTSP.me or RTSP Stream to create temporary streams
   - Example: `rtsp://demo:demo@ipvmdemo.dyndns.org:5541/onvif-media/media.amp`

### Managing Overlays

1. **Creating an Overlay**
   - While viewing a stream, click "Add Overlay"
   - Choose the overlay type (text or image)
   - Position and resize the overlay as needed
   - Click "Save" to store your overlay settings

2. **Editing Overlays**
   - Select an existing overlay from the overlay panel
   - Modify its properties (position, size, content)
   - Click "Update" to save changes

3. **Deleting Overlays**
   - Select the overlay you wish to remove
   - Click the "Delete" button
   - Confirm deletion when prompted

## API Documentation

ShieldVision provides a RESTful API for managing overlays and stream settings.

### Authentication Endpoints

- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Authenticate a user and receive a JWT token

### Camera Endpoints

- `GET /api/cameras` - Get all cameras for the authenticated user
- `POST /api/cameras` - Add a new camera
- `PUT /api/cameras/:id` - Update camera details
- `DELETE /api/cameras/:id` - Delete a camera

### Overlay Endpoints

- `GET /api/overlays` - Get all overlays for a specific camera
- `POST /api/overlays` - Create a new overlay
- `PUT /api/overlays/:id` - Update an existing overlay
- `DELETE /api/overlays/:id` - Delete an overlay

### Stream Endpoints

- `GET /video_feed?cameraUrl=<rtsp_url>` - Get video stream with object detection

## License

This project is licensed under the MIT License - see the LICENSE file for details.

This dashboard supports 4 different subscription models.

1. Free -> up to 3 cameras.

2. Essential -> up to 6 cameras.

3. Professional -> up to 12 cameras.

4. Enterprice -> up to 99 cameras.

## Testing the payment system.

For payments i decided to use the paypal api.

To try out payments you can use the following sandbox account:

- **Buyers Account Email:**: buyer@react.com
- **Buyers Account Password:** 12345678

- **Sellers Account Email:**: seller@react.com
- **Sellers Account Password:** 12345678

## Testing the surveilence system

The streaming system supports two different kind of streams.

- **http stream:** A regular http url to a camera stream of a specific camera.
- **rtsp stream:** A rtsp stream, better quality stream that needs to be relayed through the server to be able to stream it in a react project.

Password protected streams can be added like this:

( url format )
rtsp://username:password@camera_ip_address:port/video_stream

Add the url in the ( add camera input ) and click on ( Add Camera ).
When choosing to stream rtsp cameras, be mindful that the converting of the stream
will be done from the server itself. Which ofcourse is very limited because of a lack
of resources on a simple PC.

This will limit the streams to about 9 cameras at a time for a pc with around 8 cores and 16gb of Ram.

( http format )
http://camera_ip_address:port/video_stream

Add the url in the ( add camera input ) and click on ( Add Camera ).
When choosing to use http streams you are only limited by the speed
of your internet connection. And of course Ram if you open a hundred streams at the same time.

## Future changes to be made.

1. Implement clean architecture and SOLID principles.
2. Implement object detection in a scalable fashion.
3. Further extract and organize React components.
4. Further perfect mobile responsiveness.
5. Cleaner error handling.
6. Implement analytics.
7. Implement a better payment system. ( Stripe )
8. Better folder structure.

## Final notes

This is a passion project & idea for a startup i want to create.
And even though i'm not sure if it's doable, I learned so much from this project.

I't wasn't easy to build this out when 9 months pregnant and after giving birth.
But i'm greatful for all the things i learned over the course of this project.

Components kept getting smaller and compacter.
Logic keeps getting extracted further and cleaner.
And simple comments became clear documentation.

Most important of all i learned to use google/stackoverflow as a solution to all my problems.

Thanks for everything,
Sapir Ben Haim.
