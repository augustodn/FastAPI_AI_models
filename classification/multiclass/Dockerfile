FROM python:3.8

RUN pip install fastapi uvicorn tensorflow keras numpy pandas sklearn

COPY ./ /api

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

RUN wget https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
RUN python iris_training.py

ENTRYPOINT ["uvicorn"]
CMD ["app:app", "--host", "0.0.0.0"]