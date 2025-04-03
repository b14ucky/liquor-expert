FROM python:3.12
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY vector_db /app/vector_db
COPY main.py vector_db.py /app/
CMD uvicorn main:app --host 0.0.0.0 --port 8000