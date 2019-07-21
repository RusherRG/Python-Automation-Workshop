FROM python:3.6

RUN mkdir app
WORKDIR app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]
