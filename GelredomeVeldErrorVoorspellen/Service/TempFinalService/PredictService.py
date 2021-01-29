from Controller.TempFinalPackage.NewPredictor import Predictor


class PredictService:

    def __init__(self, gripperjack, part, type, data):
        self.predictor = Predictor()
        self.gripperjack = gripperjack
        self.part = part
        self.type = type
        self.data = data

    def predict(self):
        return self.predictor.predictor(self.type, self.gripperjack, self.part, self.data)

    pass
