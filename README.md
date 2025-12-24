🌦️ Professional Weather Forecasting System
A high-performance, containerized weather application built with a FastAPI backend and a Tailwind CSS frontend. This project demonstrates modern full-stack practices including rate limiting, professional logging, and Docker containerization.

🚀 Key Features
Asynchronous Backend: Built with FastAPI for high-concurrency performance.

Dockerized Architecture: Completely isolated backend environment for consistent deployment.

Rate Limiting: Integrated SlowAPI to prevent API abuse and manage costs (15 requests/min).

Professional Logging: Comprehensive error tracking using Python's logging module with persistent storage.

Self-Healing Design: Advanced error handling to mask upstream API failures and provide user-friendly feedback.

Frontend Optimization: Skeleton screens for perceived performance and localStorage for data caching.

🏗️ Architecture Overview
The system is split into two decoupled layers:

Backend (Service): A Python-based API running inside a Docker container.

Frontend (Client): A static HTML/JS/Tailwind application that communicates with the containerized service via port mapping.

🛠️ Tech Stack
Backend: Python, FastAPI, HTTPX, SlowAPI, Docker.

Frontend: JavaScript (ES6+), Tailwind CSS, HTML5.

Infrastructure: Docker Desktop (MacBook Air optimization).

🚦 Getting Started
1. Prerequisites

Docker installed on your machine.

A WeatherAPI Key (available at weatherapi.com).

2. Environment Setup

Create a .env file in the root directory (refer to .env.example):

Code snippet
WEATHER_API_KEY=your_real_api_key_here
ALLOWED_ORIGINS=http://localhost:5500,http://127.0.0.1:5500
Note: Do not use quotes or comments in the .env file to ensure Docker compatibility.

3. Build & Run with Docker

Bash
# Build the image
docker build -t weather-backend .

# Run the container in detached mode
docker run -d -p 8000:8000 --env-file .env --name weather-app weather-backend
🔍 Observability & Debugging
To monitor the background service, use the following professional commands:

Check Vitals: docker stats weather-app

View Logs: docker logs -f weather-app

Verify Environment: docker exec weather-app env
