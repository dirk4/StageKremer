import sklearn.ensemble
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

from Controller.TensorFlow.IMLTrain import IMLTrain

import pandas as pd
import tensorflow as tf

import joblib


def load_dataframe():
    csv_file = 'Recources\\combined.csv'
    dataframe = pd.read_csv(csv_file)
    dataframe.drop(dataframe.columns[dataframe.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
    dataframe = dataframe.drop(columns=['TempTimestamp'])
    dataframe = dataframe.dropna()
    return dataframe


def compile_model(model):
    optimizer = tf.keras.optimizers.Nadam()
    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mae', 'mse', 'mape'])
    return model


class MLTrain(IMLTrain):
    dataframe = load_dataframe()
    regressor = None

    x_test = None
    y_test = None

    def build_model(self):
        r = [
            ('K Neighbors Regressor', KNeighborsRegressor()),
            ('Random Forest Regressor', sklearn.ensemble.RandomForestRegressor(n_estimators=250, random_state=1, warm_start=True))
        ]
        self.regressor = sklearn.ensemble.VotingRegressor(estimators=r, verbose=1)

    def train_model(self):
        print(self.dataframe.columns)
        y = self.dataframe.pop('Tel')
        x = self.dataframe
        x_train, self.x_test, y_train, self.y_test = train_test_split(x, y, test_size=0.2, random_state=0)
        self.regressor.fit(x_train, y_train)

    def save_dataset(self):
        joblib_file = 'Saved_models\\joblib_regressor.pkl'
        joblib.dump(self.regressor, joblib_file)

    def evaluate_dataset(self):
        pass
