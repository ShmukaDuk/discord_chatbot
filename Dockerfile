# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot code into the container
COPY bot/ /app/bot/
COPY .env /app/.env
COPY data/ /app/data/

# Run the bot
CMD ["python", "bot/bot.py"]
