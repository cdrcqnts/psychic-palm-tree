FROM python:latest

ADD . /app
WORKDIR /app
RUN pip3 install fastapi uvicorn[standard] gunicorn requests
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "15400", "--reload"]