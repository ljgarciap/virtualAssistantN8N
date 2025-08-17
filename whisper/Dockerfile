FROM python:3.9-slim-bullseye

RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    faster-whisper==0.10.0 \
    flask==3.0.2

WORKDIR /app
COPY transcribe.py .

EXPOSE 9000
CMD ["python3", "transcribe.py"]