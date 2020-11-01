FROM python:3.8-alpine
LABEL org.stepik.version==v0.1

COPY requirements.txt /

RUN pip install -r requirements.txt

ADD . /
WORKDIR /

EXPOSE 1861

CMD ["gunicorn", "-w 4", "run:app"]