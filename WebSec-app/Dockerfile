FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=webapp.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc g++ musl-dev linux-headers python3-dev libffi-dev make
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
VOLUME ["../shared-volume/"]
COPY . .
# CMD ["flask", "run"]
ENTRYPOINT ["python3", "webapp.py"]