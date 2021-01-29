import pandas as pd
import pickle
from sklearn import metrics, tree
from sklearn.ensemble import VotingRegressor, RandomForestRegressor, AdaBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from Controller.TempFinalPackage.WarningChecker import WarningChecker as wc
from Controller.TempFinalPackage import PeakGenerator as pg
import os


class Trainer:
    df = pd.DataFrame

    def __init__(self, gripperjack, location, type):
        self.gripperjack = gripperjack,
        self.location = location,
        self.type = type

    def train(self):
        self.gripperjack = self.gripperjack[0]
        self.location = self.location[0]
        generator = pg.generator_factory(self.type)

        self.df: pd.DataFrame = generator.generate(self.gripperjack, self.location, 1)
        print(self.df.columns)
        self.df = self.df.drop(columns=['Timestamp']).dropna()

        print('DATAFRAME IS LOADED IN')
        x = None
        x_train = None
        x_test = None

        y = None
        y_train = None
        y_test = None

        regressor = None

        y = self.df.pop('next')

        x = self.df

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

        r = [
            ('K Neighbour Regressor', KNeighborsRegressor(n_neighbors=15, n_jobs=5, leaf_size=50)),
            ('Random Forrest Regressor', RandomForestRegressor(n_estimators=200, n_jobs=5)),
            ('Ada Regressor', AdaBoostRegressor(n_estimators=100, learning_rate=0.1))
        ]

        regressor = VotingRegressor(r, weights=[0.1, 1, 0.1])

        regressor.fit(x_train, y_train)
        print('===================')
        print('SCORE X/Y TEST')
        print(regressor.score(x_test, y_test))
        dump_location = 'Recources\\regressor_dumps\\' + self.type + '\\' + str(
            self.gripperjack) + '\\' + self.location

        print('==================')
        print('ACCURACY')
        y_pred = regressor.predict(x_test)
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mape = (mae / (y.max() - y.min())) * 100
        print('MAE')
        print(mae)
        print('MAPE')
        print(mape)

        if not os.path.exists(dump_location):
            os.makedirs(dump_location)
        pickle.dump(regressor, open(dump_location + '\\regressor.sav', 'wb'))
        return mape

    pass
