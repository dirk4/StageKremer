from Controller.TensorFlow.IMLTrain import IMLTrain

import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers


def prepare_dataframe():
    csv_file = 'Recources\\GripperjackLogs\\GP1\\ClaspPressure\\max\\5min.csv'
    dataframe = pd.read_csv(csv_file)
    dataframe.drop(dataframe.columns[dataframe.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
    dataframe = dataframe.drop(columns=['Timestamp'])
    dataframe = dataframe.dropna()
    return dataframe


def build_model(train_dataset):
    model = keras.Sequential([
        layers.Dense(128, activation='relu', input_shape=[len(train_dataset.keys())]),
        layers.Dense(512, activation=tf.keras.activations.tanh),
        layers.Dense(512, activation='selu', kernel_initializer='lecun_normal'),
        layers.Dense(1024, activation='relu'),
        layers.Dense(128, activation=tf.keras.activations.elu),
        layers.Dropout(.1),
        layers.Dense(1)
    ])
    return model

def compile_model(model):
    optimizer = tf.keras.optimizers.Nadam()
    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mae', 'mse', 'mape'])
    return model

class MLTrain(IMLTrain):
    dataframe = prepare_dataframe()
    train, test = train_test_split(dataframe, test_size=0.2)
    train, val = train_test_split(train, test_size=0.2)
    train_dataset = dataframe.sample(frac=0.8, random_state=0)
    test_dataset = dataframe.drop(train_dataset.index)
    train_labels = train_dataset.pop('to_be_predicted')
    test_labels = test_dataset.pop('to_be_predicted')
    model = build_model(train_dataset)
    model = compile_model(model)

    def train_model(self):
        EPOCHS = 300
        print(self.train_dataset)
        print(self.train_labels)
        history = self.model.fit(self.train_dataset, self.train_labels,
                                 epochs=EPOCHS, validation_split=0.2, verbose=1)
        hist = pd.DataFrame(history.history)
        hist['epoch'] = history.epoch
        hist.tail()
        print(self.model.summary())
        self.save_dataset()

    def save_dataset(self):
        self.model.save('Saved_models\\Tensorflow\\test')

    def evaluate_dataset(self):
        loss, mae, mse, mape = self.model.evaluate(self.test_dataset, self.test_labels, verbose=1)
        print(mape)
        test_predictions = self.model.predict(self.test_dataset).flatten()
        print(test_predictions)
        return str(mae)

