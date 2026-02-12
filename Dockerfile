# 1. Start with a lightweight Python base
FROM python:3.11-slim

# 2. Set the folder inside the container
WORKDIR /app

# 3. Copy the 'shopping list' and install it
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy your actual code (main.py, .env, etc.)
COPY . .

# 5. Open the port and run the server
EXPOSE 8000
CMD ["python", "main.py"]