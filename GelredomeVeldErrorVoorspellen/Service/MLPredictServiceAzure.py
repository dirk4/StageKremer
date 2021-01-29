import Controller.Azure.MLPredict as mlt
from django.http import HttpResponse
import json

class MLTrainService():
    def predict_page_view(self, request, num):
        m = mlt.MLPredict(num)
        m.load_model()
        return HttpResponse(m.prediction())