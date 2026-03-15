FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# This line is the secret! It copies your image folder into Docker
COPY static/ /app/static/
COPY templates/ ./templates/
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]