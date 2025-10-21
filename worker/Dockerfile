FROM python:3.10-slim

WORKDIR /app
COPY . .

# Install all dependencies required by OpenCV and ffmpeg for video streaming
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0 \
        libgthread-2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install dependencies with better timeout handling
RUN pip install --upgrade pip
RUN pip install --timeout=200 --retries=5 -r requirements.txt

ENV PYTHONPATH=/app
EXPOSE 7000

CMD ["python", "-m", "src.main"]
