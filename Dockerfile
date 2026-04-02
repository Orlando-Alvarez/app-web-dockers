FROM python:3.13
WORKDIR /app
COPY app.py .
RUN pip install flask redis
ENV PYTHONUNBUFFERED=1
CMD ["python", "app.py"]