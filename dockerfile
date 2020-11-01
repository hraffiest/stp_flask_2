FROM python:3.8-alpine
LABEL org.stepik.version==v0.1

WORKDIR /test_project
ADD . /test_project

RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 1861

CMD ["gunicorn", "-w 4", "run:app"]