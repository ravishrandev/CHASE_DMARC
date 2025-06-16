#use official Python image
FROM python:3.11-slim

#Set working direcotry in the container
WORKDIR /app

#Copy everything into the container
COPY . .

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Default command
CMD ["python", "main.py"]