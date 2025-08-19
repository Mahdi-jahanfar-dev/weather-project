# 🌤️ Weather Project

A lightweight system for fetching and storing weather data using **Celery** and **Redis**.  

This project collects weather information for multiple cities every **15 minutes** via the **OpenWeather API** and stores the results in **Redis**. Scheduled tasks are managed by **Celery Beat**, and execution is handled by **Celery Worker**. It's designed as a background worker system, perfect for periodic updates and scalable processing.

> ⚠️ Note: This project currently focuses on background tasks only and does not provide an HTTP API.

---

## 🚀 Features

- ⏱️ Automatic weather fetching every 15 minutes with **Celery Beat**  
- ⚡ Asynchronous task execution with **Celery Worker**  
- 💾 Storing results in **Redis** for fast access  
- 🐳 Ready for Docker: `Dockerfile` and `docker-compose.yml` included  
- 🛠️ Easy to extend: Add new cities or data sources effortlessly  

---

## 🏗️ Architecture


- **Beat:** Schedules tasks periodically.  
- **Worker:** Executes tasks, fetches weather, and stores results in Redis.  
- **Redis:** In-memory storage for fast reads.

---

## 📦 Requirements

- **Docker & Docker Compose** (recommended)  
  OR:  
- **Python 3.11+**, **Redis**, **Celery** installed locally  
- **OpenWeather API key** (free at [OpenWeather](https://openweathermap.org/api))

---

## 🐳 Quick Start with Docker Compose

1. Create `.env` file and add your API key:

```bash
echo "OPENWEATHER_API_KEY=YOUR_API_KEY_HERE" > .env
```
2. Running the Project:
```bash
sudo docker-compose up --build
