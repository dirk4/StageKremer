from django.http import HttpResponse
import Controller.TensorFlow.MLTrain as mlt

class MLTrainService():
    m = mlt.MLTrain()


    def train_page_view(self, request):
        self.m.train_model()
        ac = self.m.evaluate_dataset()
        self.m.save_dataset()
        htmlResponse = str(ac)
        return HttpResponse(htmlResponse)
