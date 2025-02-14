# Use the official Python image
FROM python:3.11-slim

# Install required tools
RUN apt-get update && apt-get install -y nginx

# Copy project files
WORKDIR /app
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy Nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the port for Nginx
EXPOSE 80

# Run Nginx and FastAPI together
CMD service nginx start && uvicorn main:app --host 0.0.0.0 --port 8000
