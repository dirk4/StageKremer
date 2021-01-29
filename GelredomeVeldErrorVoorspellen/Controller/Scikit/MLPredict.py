import joblib
import pandas as pd

from Controller.TensorFlow.IMLPredict import IMLPredict


class MLPredict(IMLPredict):

    data = None
    num = 4
    regressor = None


    def load_model(self):
        self.regressor = joblib.load('Saved_models\\SciKit\\joblib_regressor.pkl')
        return self.regressor

    def load_data(self,num):
        self.data = pd.read_csv("Recources\\CSVLog\\LogCSV" + str(num) + ".csv")
        self.data = self.data.fillna(0)
        self.data = self.data.drop(columns=['TempTimestamp', 'Tel'])

    def prediction(self):
        print(self.data)
        self.load_model()
        prediction = self.regressor.predict(self.data)
        totaal = 0
        for i in prediction:
            totaal += float(i)
        totaal /= len(prediction)
        print(totaal)
        return totaal
