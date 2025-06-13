# Use official Python image
FROM python:3.12.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "backend.py"]
