import pickle
import pandas as pd
import os

from Controller.SciKitDynamic.DataframeHandler import DataframeHandler
from Controller.SciKitDynamic.ModelHandler import ModelHandler


class Predict:
    model_handler = ModelHandler()
    dataframe_handler = DataframeHandler()

    dataframe = None

    def __init__(self):
        self.regressor = self.model_handler.load_model()
        self.dataframe = self.dataframe_handler.load_dataframe(1, 'Velocity', 'max', '5min')
        self.dataframe.drop(columns=['Timestamp', 'to_be_predicted']).dropna()

    def prediction(self): 
        return self.regressor.predict(self.dataframe)
        pass

    pass


