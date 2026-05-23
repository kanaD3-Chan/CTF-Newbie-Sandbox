FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libnss3 libnspr4 libatk-bridge2.0-0 libdrm2 \
    libxkbcommon0 libxcomposite1 libxdamage1 \
    libxrandr2 libgbm1 libpango-1.0-0 \
    libcairo2 libasound2 libatspi2.0-0 && \
    apt-get clean

RUN pip install flask playwright --no-cache-dir
RUN playwright install chromium --with-deps

WORKDIR /app
COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]
