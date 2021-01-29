from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv(
    'C:\\Users\Lukassen\PycharmProjects\GelredomeVeldErrorVoorspellen\Recources\Volledige_Gelredome_Data_CSV.csv')

print(data)

plt.plot(data['GP1_PushPressure'], label='GP1')
plt.plot(data['GP2_PushPressure'], label='GP2')
plt.plot(data['GP3_PushPressure'], label='GP3')
plt.plot(data['GP4_PushPressure'], label='GP4')
plt.legend()
plt.show()