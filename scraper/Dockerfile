FROM python:3.7-stretch

WORKDIR /opt/scraper/src

COPY src/requirements.txt /opt/scraper/src/requirements.txt
RUN pip install -r requirements.txt

COPY src/ /opt/scraper/src/
RUN pip install -e .

ENTRYPOINT ["python", "-u", "scraper/__init__.py"]
