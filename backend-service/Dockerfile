FROM python

RUN mkdir /service
COPY . /service/backend-service/

WORKDIR /service/backend-service
RUN pip install -r requirements.txt

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
