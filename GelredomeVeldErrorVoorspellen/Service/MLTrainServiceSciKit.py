from django.http import HttpResponse
import Controller.Scikit.MLTrain as mlt


class MLTrainService():
    m = mlt.MLTrain()

    def train_page_view(self):
        self.m.build_model()
        self.m.train_model()
        self.m.save_dataset()
        return HttpResponse('Model has been saved')
