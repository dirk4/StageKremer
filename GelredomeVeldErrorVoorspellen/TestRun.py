import requests
import pandas as pd
import time
import json
from matplotlib import pyplot as plt
import numpy as np
import datetime

gripperjack = "1"
part = "ClaspPressure"


url = "http://127.0.0.1:8000/predictModel/"

json_data = np.load('C:\\Users\\Lukassen\\PycharmProjects\\GelredomeVeldErrorVoorspellen\\Recources\\lastValues.npy')

json_data = []

json_data = np.save('C:\\Users\\Lukassen\\PycharmProjects\\GelredomeVeldErrorVoorspellen\\Recources\\lastValues.npy', json_data)
df = pd.read_csv('Recources\\Volledige_Gelredome_Data_CSV.csv')
# print(df.transpose().to_json())

datasets = []

# print(df.to_json())
for i in range(0, 50):
    json_string = """{
    "gripperjack": \"""" + gripperjack + """\",
    "part":  \"""" + part + """\",
    "type": "peak",
    "data": """
    json_string += df.loc[i + 100].to_json() + "},"
    print(json_string)
    datasets.append(json_string)

print(datasets)
# responses = []
# times = []
# x = []
# fig = plt.gcf()
# fig.show()
# fig.canvas.draw()
#
#
# for data in datasets:
#     if len(x) is 0:
#         x.append(0)
#     else:
#         x.append(max(x)+1)
#     response = requests.post(url, data).json()
#     print(response)
#     responses.append(float(response['prediction']))
#     times.append(response['time'])
#     plt.xticks(x, times)
#     plt.plot(x, responses)
#
#     fig.canvas.draw()
# plt.pause(10)
