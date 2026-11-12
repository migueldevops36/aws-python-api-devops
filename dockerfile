FROM python:3.12-slim
WORKDIR /app
COPY app.py .
ENV APP_HOST=0.0.0.0
EXPOSE 8000
CMD ["python3", "app.py"]
