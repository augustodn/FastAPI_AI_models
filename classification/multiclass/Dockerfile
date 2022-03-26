FROM python:3.8

RUN pip install fastapi uvicorn tensorflow keras numpy

COPY ./ /api

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["app:app", "--host", "0.0.0.0"]