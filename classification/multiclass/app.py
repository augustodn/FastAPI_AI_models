import uvicorn
from fastapi import FastAPI
from keras.models import load_model
import numpy as np

# init app
app = FastAPI()

model = load_model("iris_model.h5")

# Routes
@app.get('/')
async def index():
    return {'text': 'Hello World!'}

@app.get('/predict/')
async def get_items(
    sepal_l: float, sepal_w: float,
    petal_l: float, petal_w: float):

    classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

    predictions = model.predict(
        [[sepal_l, sepal_w, petal_l, petal_w]])
    position = int(np.argmax(predictions))
    probability = float(np.max(predictions))
    class_predicted = classes[position]

    return {'prediction': class_predicted,
            'probability': probability,
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)