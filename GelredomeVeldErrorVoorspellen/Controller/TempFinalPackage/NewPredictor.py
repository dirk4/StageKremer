import os
import pickle

import numpy as np
import pandas as pd
from sklearn.ensemble import VotingRegressor

from Controller.TempFinalPackage.WarningChecker import WarningChecker as wc


def add_to_json(data):
    try:
        np_array = np.load('C:\\Users\\Lukassen\\PycharmProjects\\GelredomeVeldErrorVoorspellen\\Recources\\lastValues.npy')
        np_array = np.append(np_array, data[0])
        np.save('C:\\Users\\Lukassen\\PycharmProjects\\GelredomeVeldErrorVoorspellen\\Recources\\lastValues.npy', np_array)

    except:

        np.save('C:\\Users\\Lukassen\\PycharmProjects\\GelredomeVeldErrorVoorspellen\\Recources\\lastValues.npy', data)


def make_dataframe(data):
    a = []
    b = []
    for i in data:
        a.append(i)
        b.append(data[i])
    df: pd.DataFrame = pd.DataFrame(columns=a)

    print(df.columns)
    df = df.append(data, ignore_index=True)
    df = df.drop(columns=['Timestamp'])
    print(df.columns)
    print(df.transpose())

    return df


class Predictor:
    regressor: VotingRegressor

    def predictor(self, version, location, part, data):
        print('start')

        dump_location = 'Recources\\regressor_dumps\\' + str(version) + '\\' + str(
            location) + '\\' + part + '\\regressor.sav'
        if not os.path.exists(dump_location):
            print('FILE NOT EXISTENT')

        self.regressor = pickle.load(open(dump_location, 'rb'))

        y_pred = self.regressor.predict(make_dataframe(data))

        print(y_pred)
        add_to_json(y_pred)
        errors = wc.check_all(y_pred, part)

        return y_pred, errors
