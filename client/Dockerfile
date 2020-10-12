FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt
COPY ./ /app
CMD ["python","client.py"]