from Controller.TempFinalPackage.NewTrainer import Trainer


class TrainService:

    def __init__(self, gripperjack, part, type):
        print(gripperjack)
        print(part)
        self.trainer = Trainer(gripperjack, part, type)

    def train(self):
        return self.trainer.train()

    pass
