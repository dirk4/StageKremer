import pandas as pd

csv = pd.read_csv(
    'C:\\Users\Lukassen\PycharmProjects\GelredomeVeldErrorVoorspellen\Recources\Volledige_Gelredome_Data_CSV.csv')

print(csv)
print(csv.columns)
pressureA = csv['GP1_PressureA']
pressureB = csv['GP1_PressureB']
pushPressure = csv['GP1_PushPressure']
claspPressure = csv['GP1_ClaspPressure']

csv['Difference'] = pressureA-pressureB

df = csv[['GP1_PressureA', 'GP1_PressureB', 'GP1_PushPressure', 'Difference']]
print(df)
