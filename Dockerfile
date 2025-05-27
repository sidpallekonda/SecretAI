# Base image with Python and GUI support
FROM python:3.10-slim

# Install required packages for tkinter and GUI
RUN apt-get update && \
    apt-get install -y python3-tk libglib2.0-0 libsm6 libxrender1 libxext6 && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the project files
COPY . .

# Default command to run the GUI
CMD ["python", "main.py"]




