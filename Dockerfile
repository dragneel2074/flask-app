# Use an official Python runtime based on Linux
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's code
COPY . .

# Expose port 8080 (or the port Render uses)
EXPOSE 8080

# Debug: Print a message when the container starts
CMD echo "Starting Flask app with Gunicorn" && \
    gunicorn app:app --bind 0.0.0.0:8080 --workers 4 --timeout 120 