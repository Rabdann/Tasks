FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /backend
COPY backend /backend/
COPY requirements.txt /backend/
RUN pip install -r requirements.txt