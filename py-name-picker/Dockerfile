FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /app

RUN apt-get update
RUN apt-get install -y gcc python3-dev
RUN pip install -r requirements.txt

CMD exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]