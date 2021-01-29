from django.http import HttpResponse

import Controller.Scikit.MLPredict as mlp


class MLPredictServiceSciKit():
    ml = mlp.MLPredict()

    def predict_view_page(self, num):
        self.ml.load_model()
        self.ml.load_data(num)
        prediction = self.ml.prediction()
        return HttpResponse(prediction)