from keras.models import load_model


model = load_model("iris_model.h5")
model.summary()