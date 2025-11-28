FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (adjust as needed)
RUN apt-get update && apt-get install -y build-essential gcc libpq-dev

# Copy requirements first
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . /app

EXPOSE 8000

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]

