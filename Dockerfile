# Use the official Python 3.10 slim image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port your Flask app runs on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
