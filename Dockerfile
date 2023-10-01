# Use an official Python runtime as a parent image
FROM python:3.8.2

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=e_voting.settings

# Create and set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN pip install --upgrade pip

# Expose the port the app runs on
# EXPOSE 8000

# Run the application
CMD gunicorn daostore:application --bind 0.0.0.0:$PORT
