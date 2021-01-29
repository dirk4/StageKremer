from Controller.TensorFlow.IMLPredict import IMLPredict


import tensorflow as tf
import pandas as pd


class MLPredict(IMLPredict):

    def __init__(self, num):
        self.num = num
        print("MLPredict has been __init__ with num: " + str(self.num))
    data = None
    num = 0
    model = None


    def load_model(self):
        self.model = tf.keras.models.load_model('Saved_models\\Tensorflow')

        return self.model

    def load_data(self):
        self.data = pd.read_csv("Recources\\CSVLog\\LogCSV" + str(self.num) + ".csv")
        self.data = self.data.fillna(0)
        self.data = self.data.drop(columns=['TempTimestamp', 'Tel'])

    def prediction(self):
        self.load_data()
        print(self.num)
        print(self.data)
        self.load_model()
        prediction = self.model.predict(self.data)
        totaal = 0
        for i in prediction:
            totaal += float(i)
        totaal /= len(prediction)
        print(totaal)
        return totaal
