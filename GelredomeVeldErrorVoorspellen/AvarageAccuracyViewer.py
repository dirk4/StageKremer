from Controller.SciKitDynamic.DynamicCsvConverter import DynamicCsvConverter
from Controller.SciKitDynamic.Train import Train

parts = ['Position', 'Velocity', 'PushPressure', 'PressureA', 'PressureB', 'ClaspPressure', 'OilTemperature']

totalMAE = 0
totalMAPE = 0
times = 0

train = Train(str(1), 'ClaspPressure', 'max', '5min')
train.create_model()
train.load_data()
train.train_model()
with open('1.txt', 'w') as f:
    f.write('[')
    for item in train.dataframe['GPV_Position'].to_list():
        f.write(str(round(item, 2)) + ', ')
    f.write(']')
accuracy = train.accuracy()
totalMAE += accuracy[0]
totalMAPE += accuracy[1]
times += 1

print('AVG MAE: ' + str(totalMAE / times))
print('AVG MAPE: ' + str(totalMAPE / times))
