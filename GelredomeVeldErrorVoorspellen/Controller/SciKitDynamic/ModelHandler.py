import pickle

from sklearn.ensemble import VotingRegressor, RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor


class ModelHandler:
    regressor = None

    def build_model(self):
        r = [('Random Forrest Regressor', RandomForestRegressor(n_estimators=100, random_state=1)),
             ('K neighbors Regressor', KNeighborsRegressor())]
        self.regressor = VotingRegressor(r)
        return self.regressor

    def load_model(self,
                   location='C:\\Users\\Lukassen\\PycharmProjects\\GelredomeVeldErrorVoorspellen\\Saved_models\\test.pkl'):
        file = open(location, 'rb')
        self.regressor = pickle.load(file)
        return self.regressor

    def save_model(self):
        pickle.dump(self.regressor, open('Saved_models\\test.pkl', 'wb'))
        pass


