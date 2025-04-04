FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY vector_db vector_db
COPY main.py vector_db.py ./
CMD uvicorn main:app --host 0.0.0.0 --port 8000
