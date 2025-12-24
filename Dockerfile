# 1. Start with a lightweight Python base
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only requirements first to optimize build speed
COPY requirements.txt .

# 4. Install dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your backend code (main.py, etc.)
COPY . .

# 6. Tell Docker which port the app listens on
EXPOSE 8000

# 7. Start the server (using 0.0.0.0 to allow external access)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]