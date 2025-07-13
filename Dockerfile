# Use official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your calculator script into the container
COPY 1-calculator.py .

# Set the default command to run the calculator
CMD ["python", "1-calculator.py"]
