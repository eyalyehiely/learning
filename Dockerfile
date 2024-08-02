# Use the official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=backend.settings
ENV PYTHONPATH=/app

# Command to run Gunicorn
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]