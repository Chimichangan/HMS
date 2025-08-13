FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1             PYTHONUNBUFFERED=1

WORKDIR /app

# Install build deps (psycopg2 etc.)
RUN apt-get update && apt-get install -y --no-install-recommends             build-essential libpq-dev gcc             && rm -rf /var/lib/apt/lists/*

# Install requirements
COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Copy project
COPY backend /app/backend

WORKDIR /app/backend
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
