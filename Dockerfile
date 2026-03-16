# Use official Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies (if any)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port (handled by Cloud Run)
EXPOSE 8080

# Environment variables for Cloud Run
ENV HOST=0.0.0.0
ENV PORT=8080

# Set SSL_CERT_FILE for certifi (installed via requirements)
# The application handles this in main.py, but it doesn't hurt to set it here too
ENV SSL_CERT_FILE=/usr/local/lib/python3.12/site-packages/certifi/cacert.pem

# Command to run the application
CMD ["python", "app/main.py"]
