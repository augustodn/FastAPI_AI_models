# Installation
`pip install fastapi uvicorn`

Besides that, in order to train the model is important to have tensorflow
installed.

# Train the model
`python iris_training.py`

# Running Server
Placed on the app.py folder execute
`$ uvicorn app:app --reload`
Open browser at: `http://127.0.0.1:8000`

# Test the model
Enter the following GET request in the browser:

[http://127.0.0.1:8000/predict/?sepal_l=1.1&sepal_w=4.3&petal_l=2.1&petal_w=3.1](http://127.0.0.1:8000/predict/?sepal_l=1.1&sepal_w=4.3&petal_l=2.1&petal_w=3.1)

Alternatively, execute the following command from the CLI:

``$ curl -X 'GET' \
  'http://127.0.0.1:8000/predict/?sepal_l=1.1&sepal_w=4.3&petal_l=2.1&petal_w=3.1' \
  -H 'accept: application/json'``

Or use your favourite API platform such as [Postman](https://www.postman.com/)

# Build Docker container

In order to generate a Docker container and launch the model, first build the 
Docker Image.

`$ docker-compose up --build`

Then you can make requests to the API accesing from localhost as explained before
in the `Test the model` section.

* * *
njoy and have fun!