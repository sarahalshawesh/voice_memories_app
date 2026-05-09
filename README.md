# Remember Me

Remember Me is a full-stack web app for collecting and comparing family oral memories. The project was inspired by a desire to preserve my mothers memories for my son and an interest in how we all remember the same events differently. 

How to use
A user selects a prompt and records their associated memory. The recording can then be played back and uploaded to a backend, where it is validated and stored.

This project is a learning project to practice full-stack development with React, TypeScript, Python and FastAPI.


## Project Purpose

The aim of this project is to understand how a frontend and backend work together in a real application.

The core technical flow:

1. Request microphone permission in the browser
2. Record audio using the MediaRecorder API
3. Playback the recording before upload
4. Send the audio file to a Python backend
5. Validate the uploaded file
6. Save the file with a unique filename
7. Return a structured response to the frontend

## Tech Stack

### Frontend

Next.js
React
TypeScript
Browser MediaRecorder API

### Backend

Python
FastAPI
Uvicorn


## Current Features

- Record audio in the browser
- Stop and save a recording
- Playback the recording before upload
- Upload the recording to the backend
- Validate allowed audio file types
- Generate a unique storage filename
- Save uploaded files locally
- Return upload metadata as JSON


Additional features will be added 


## What I Have Learned

Through this project, I have been learning:

- How React state controls the user interface
- How to use browser APIs such as `MediaRecorder`
- How to send files from a frontend to a backend using `FormData`
- How FastAPI handles routes and file uploads
- How to validate uploaded files by content type and extension
- How to structure backend code into routes, services and config
- How to debug Python import issues and circular imports
- How local development differs from deployment environments


## Project Structure

Example structure:

```txt
remember-me/
├── frontend/
│   ├── app/
│   ├── components/
│   ├── package.json
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── routers/
│   │   ├── services/
│   │   ├── database/
│   ├── uploads/
│   ├── requirements.txt
│
└── README.md