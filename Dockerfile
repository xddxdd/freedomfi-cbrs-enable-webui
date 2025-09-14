# Use the official lightweight Python image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the script into the container
COPY tr069.py .

# Expose the port the server will run on
EXPOSE 8443

# Run the script when the container starts
CMD ["python", "tr069.py"]