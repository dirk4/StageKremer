import pickle as pk
import pandas as pd
from sklearn.ensemble import VotingRegressor
from Controller.TempFinalPackage.PeakGenerator import generator_factory
from pylab import plt

peak_type = 'peak'
gripperjack = 1
part = 'ClaspPressure'

generator = generator_factory(peak_type)
generator.csv = csv = pd.read_csv(
    'C:\\Users\\Lukassen\\PycharmProjects\\GelredomeVeldErrorVoorspellen\\Recources\\Volledige_Gelredome_Data_CSV.csv')
df: pd.DataFrame = generator.generate(gripperjack, part, 1)
to_predict = df['next']
print(df.columns)
df = df.dropna().drop(columns=['Timestamp', 'next'])

regressor: VotingRegressor = pk.load(open(
    'C:\\Users\\Lukassen\\PycharmProjects\\GelredomeVeldErrorVoorspellen\\Recources\\regressor_dumps\\' + peak_type + '\\' + str(
        gripperjack) + '\\' + part + '\\regressor.sav', 'rb'))

prediction = regressor.predict(df)
df['predicted'] = prediction
df['to_predict'] = to_predict
print(df[['predicted', 'to_predict']])

plt.plot(df['predicted'], label='predicted')
plt.plot(df['to_predict'], label='actual')
plt.legend()
plt.show()
