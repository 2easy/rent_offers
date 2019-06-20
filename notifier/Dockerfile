FROM python:3.7-stretch

WORKDIR /opt/notifier/src

COPY src/requirements.txt /opt/notifier/src/requirements.txt
RUN pip install -r requirements.txt

COPY src/ /opt/notifier/src/
RUN pip install -e .

ENTRYPOINT ["python", "-u", "notifier/__init__.py"]
