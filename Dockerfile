# 1. Use Python as the base
FROM python:3.9-slim

# 2. Create a folder for the app inside the container
WORKDIR /app

# 3. Copy your project files from your PC into the container
COPY . /app

# 4. Install the web framework
RUN pip install flask

# 5. Tell the container to listen on port 5000
EXPOSE 5000

# 6. The command to start your app
CMD ["python", "app.py"]