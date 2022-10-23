FROM python

RUN mkdir /service
COPY . /service/backend-service/

WORKDIR /service/backend-service
RUN pip install -r requirements.txt

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0"]
