# Use an official lightweight Ubuntu image with Python 3.11
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3.11 python3-pip && \
    python3.11 -m pip install --upgrade pip

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV OPENAI_API_KEY=your_openai_api_key_here
ENV OPENAI_MODEL=gpt-3.5-turbo

# Run uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
