FROM python:3.8.10-slim

COPY . /app
WORKDIR /app

#RUN python3 -m venv /opt/venv

RUN pip install pip --upgrade
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh
RUN chmod +x migrate.sh
RUN /app/migrate.sh

CMD ["/app/entrypoint.sh"]
