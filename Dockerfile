FROM python:2-alpine

USER root

COPY ./ /opt/phoenix

WORKDIR /opt/phoenix

RUN pip install -r requirements.txt

CMD [ "python", "src" ]