# 🌦️ Containerized Weather Forecasting System

A professional, full-stack weather application featuring a high-performance **FastAPI** backend and a responsive **Tailwind CSS** frontend. This project is engineered to handle real-world challenges like API rate limiting, network latency, and environment isolation.



## 🎓 What I Learned (Senior Engineering Competencies)

Throughout this project, I transitioned from writing simple scripts to building a **resilient microservice**. Key takeaways include:

* **Asynchronous Programming**: Leveraged Python's `async/await` and `httpx` to handle non-blocking API calls, ensuring the server stays responsive under load.
* **Containerization & DevOps**: Mastered **Docker** to package the backend, ensuring "Environment Parity" (it works the same on my MacBook as it does in the cloud).
* **System Observability**: Implemented a professional **Logging Architecture** to capture raw upstream errors for debugging while providing clean, helpful feedback to the user.
* **Defensive Design**: Integrated **Rate Limiting** (SlowAPI) to protect resources and used **Skeleton Screens** to improve perceived performance during network latency.
* **Security & Configuration**: Applied strict **Environment Variable** management using `.env` files and `.gitignore` to protect sensitive API credentials.

---

## 🏗️ Architecture

The application follows a decoupled architecture:
* **Backend**: Containerized FastAPI service.
* **Frontend**: Static HTML/JS/Tailwind client.
* **Communication**: Restful API calls over a Docker-to-Host bridge (Port 8000).

---

## 🛠️ Tech Stack

* **Backend**: Python 3.11, FastAPI, HTTPX, SlowAPI, Uvicorn
* **Frontend**: Tailwind CSS, Vanilla JavaScript
* **Infrastructure**: Docker Desktop (MacBook Air optimization)

---

## 🚀 Deployment & Usage

### 1. Setup Environment
Create a `.env` file in the root directory. **Crucial:** Do not use quotes or comments on the same line as your keys to ensure Docker compatibility.

```env
WEATHER_API_KEY=your_key_here
ALLOWED_ORIGINS=http://localhost:5500,[http://127.0.0.1:5500](http://127.0.0.1:5500)
```
# Build the image
docker build -t weather-backend .

# Run in detached mode
docker run -d -p 8000:8000 --env-file .env --name weather-app weather-backend

## 3. Monitoring & Management

View Live Logs: docker logs -f weather-app

Check Resource Usage: docker stats weather-app

Stop Container: docker stop weather-app


---

### 📝 Your Final Portfolio Checklist
* **Visual Proof**: If you can, take a screenshot of your app running with data for Jaipur and Mumbai and add it to the top of the README.
* **Sync to GitHub**: Once you save this file, run:
    1. `git add README.md`
    2. `git commit -m "docs: add professional README with architecture and learnings"`
    3. `git push`

**Would you like me to show you how to add a "License" file to your repository?** It's a small detail, but it makes your project look like a serious open-source contribution to anyone viewing your profile.
