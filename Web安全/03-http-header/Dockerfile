FROM python:3.11-alpine
RUN pip install flask --no-cache-dir
WORKDIR /app
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
