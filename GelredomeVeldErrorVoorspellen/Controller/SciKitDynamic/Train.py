from sklearn import metrics
from sklearn.model_selection import train_test_split

from Controller.SciKitDynamic.DataframeHandler import DataframeHandler
from Controller.SciKitDynamic.ModelHandler import ModelHandler


class Train:
    x = None
    x_train = None
    x_test = None

    y = None
    y_train = None
    y_test = None

    regressor = None

    def __init__(self, location=None, part=None, value_type=None, time_interval=None):
        self.model_handler = ModelHandler()
        self.dataframe_handler = DataframeHandler()

        self.location = location
        self.part = part
        self.value_type = value_type
        self.time_interval = time_interval
        self.regressor = self.model_handler.build_model()

    def print_training_info(self):
        print('==============')
        print('TRAINING:')
        print('\tGP' + self.location)
        print('\t' + self.part)
        print('\t' + self.value_type)
        print('\t' + self.time_interval)
        print('==============')

    def split_data(self):
        df = self.dataframe_handler.load_dataframe(self.location, self.part, self.time_interval, self.value_type)
        self.y = df.pop('to_be_predicted').copy()
        self.x = df
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.2,
                                                                                random_state=1)

    def train_model(self):
        self.regressor.fit(self.x_train, self.y_train)

    def test_prediction(self):
        return self.regressor.predict(self.x)

    def accuracy(self):
        y_pred = self.regressor.predict(self.x_test)
        mae = metrics.mean_absolute_error(self.y_test, y_pred)
        mape = (mae / (self.y.max() - self.y.min())) * 100
        return mae, mape

    def reliability(self):
        accurate = 0
        y_pred = self.regressor.predict(self.x_test)
        for _ in y_pred:
            if -0.5 < y_pred - self.y_test > 0.5:
                accurate = +1
        reliability = accurate / len(y_pred) * 100
        return reliability


