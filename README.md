# Installation
`pip install fastapi uvicorn`

Besides that, in order to train the model is important to have tensorflow
installed.

# Download the dataset

In this project we'll use the iris dataset. It's a simple toy dataset which
we'll help us understand the `MLOps` flow. Download it from:


[Iris Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)

Alternatively, you can execute the following command in the same folder where
`iris_training.py` is placed:

`$ wget https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data`

# Train the model
`python iris_training.py`

# Running the Server
Placed on the app.py folder execute
`$ uvicorn app:app --reload`

Open browser at: `http://127.0.0.1:8000`

# Get Model Predictions
Enter the following GET request in the browser:

[http://127.0.0.1:8000/predict/?sepal_l=1.1&sepal_w=4.3&petal_l=2.1&petal_w=3.1](http://127.0.0.1:8000/predict/?sepal_l=1.1&sepal_w=4.3&petal_l=2.1&petal_w=3.1)

Alternatively, execute the following command from the CLI:

``$ curl -X 'GET' 'http://127.0.0.1:8000/predict/?sepal_l=1.1&sepal_w=4.3&petal_l=2.1&petal_w=3.1' -H 'accept: application/json'``

<br>

Or use your favourite API platform such as [Postman](https://www.postman.com/)

# Build a Docker container

The Docker image will download the dataset, train the model, store it and serve
it as a REST API.

`$ docker-compose up --build`

Then you can make requests to the API accesing from localhost as explained before
in the [Get Model Predictions](#get-model-predictions) section.

* * *
njoy and have fun!