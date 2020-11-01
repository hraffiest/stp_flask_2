FROM python:3.8-alpine
LABEL org.stepik.version==v0.1

ADD . /test_project
WORKDIR /test_project

RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 1861

CMD ["gunicorn", "-w 4", "run:app"]