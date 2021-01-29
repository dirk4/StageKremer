from Controller.SciKitDynamic.DynamicCsvConverter import DynamicCsvConverter
import numpy as np
from yellowbrick.target import FeatureCorrelation
import pandas as pd

values = []
from Controller.TempFinalPackage.PeakGenerator import generator_factory


def showCorrelation(gripperjack_nr, part):
    data = DynamicCsvConverter(gripperjack_nr, part, '5min', 'max',
                               pd.read_csv(
                                   'C:\\Users\\Lukassen\\PycharmProjects\\GelredomeVeldErrorVoorspellen\\Recources\\Volledige_Gelredome_Data_CSV.csv',
                                   index_col=False))
    data = data.make_file()

    # to see correlation with the to be predicted remove 'to_be_predicted' from drop columns and put the 'to_be_predicted variable in the data.pop method'
    data = data.drop(columns=['Timestamp'])
    data = data.dropna()
    y = data.pop('to_be_predicted')
    X = data

    # Create a list of the feature names
    features = np.array(data.columns)

    # Create a list of the discrete features
    discrete = [False for _ in range(len(features))]
    discrete[1] = True

    # Instantiate the visualizer
    visualizer = FeatureCorrelation(labels=features, size=(1200, 700))
    visualizer.title = part
    visualizer.fit(X, y)
    values.append(visualizer.scores_)
    visualizer.show()


parts = ['Position', 'Velocity', 'PushPressure', 'PressureA', 'PressureB', 'ClaspPressure', 'OilTemperature']
for j in parts:
    showCorrelation(1, j)
    print(values)
