# Use official Python image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PKG_CONFIG_PATH=/usr/lib/pkgconfig:/usr/local/lib/pkgconfig
ENV FLASK_APP=/app/myproject/app.py  
ENV FLASK_ENV=development

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsystemd-dev \
    pkg-config \
    libsystemd0 \
    cups \
    libcups2-dev \
    libgirepository1.0-dev \
    gir1.2-gtk-3.0 \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/* 
# Copy project files
COPY Flask/project/myproject /app/myproject
COPY Flask/project/requirements.txt /app/

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
