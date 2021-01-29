from django.http import HttpResponse
import Controller.TensorFlow.MLPredict as mlp
import json

class MLPredictService():
    m = None

    def predict_page_view(self, num):
        self.m = mlp.MLPredict(num)
        return HttpResponse(self.m.prediction())
