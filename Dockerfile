# Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Command to run the app
CMD ["python", "app/app.py"]
