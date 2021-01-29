from Controller.SciKitDynamic.Train import Train


class SciKitDynamicService:
    mlt = None

    def __init__(self, location=None, part=None, value_type=None, time_interval=None):
        self.mlt = Train(location, part, value_type, time_interval)

    def train_page_view(self):
        self.mlt.split_data()
        self.mlt.print_training_info()
        self.mlt.train_model()
        return self.mlt.accuracy()

    def graph_info(self):
        self.mlt.split_data()
        self.mlt.print_training_info()
        self.mlt.train_model()
        return self.mlt.test_prediction().tolist()
