# multi-class classification with Keras
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


# load dataset
dataframe = pd.read_csv("iris.data", header=None)
dataset = dataframe.values
X = dataset[:,0:4].astype(float)
Y = dataset[:,4]
# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

# define baseline model
def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(8, input_dim=4, activation='relu'))
    model.add(Dense(3, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

model = baseline_model()

# Split dataset in train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, dummy_y, test_size=0.2, random_state=42)

model.fit(
    X_train, y_train, epochs=200, batch_size=5,
    verbose=0, shuffle=True
)

scores = model.evaluate(X_test, y_test, verbose=0)
print(f"{model.metrics_names[1]}: {scores[1]*100}")

model.save('iris_model.h5')