FROM python:alpine3.15
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python3", "api-handler.py"]