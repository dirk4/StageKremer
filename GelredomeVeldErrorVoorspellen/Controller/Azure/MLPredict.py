from Controller.TensorFlow.IMLPredict import IMLPredict

from Controller.TensorFlow.MLTrain import MLTrain

import tensorflow as tf
import urllib
import json
# If you are using Python 3+, import urllib instead of urllib2

import json
import pandas as pd


class MLPredict(IMLPredict):
    model = None
    data = None
    ya = None
    ya1 = None
    num = 0

    def __init__(self, num):
        self.num = num

    def load_model(self):
        self.data = pd.read_csv("Recources\\CSVLog\\LogCSV" + str(self.num) + ".csv")
        self.ya = self.data.fillna(17)
        print(self.data.columns)
        print(self.ya)
        self.ya = self.ya.values.tolist()
        print(self.ya)

    def prediction(self):

        data = {

            "Inputs": {

                "input1":
                    {
                        "ColumnNames": ["GPV_Position", "GPV_Velocity", "GP1_Position", "GP1_Velocity",
                                        "GP1_PushPressure", "GP1_PressureA", "GP1_PressureB", "GP1_ClaspPressure",
                                        "GP1_OilTemperature", "GP2_Position", "GP2_Velocity", "GP2_PushPressure",
                                        "GP2_PressureA", "GP2_PressureB", "GP2_ClaspPressure", "GP2_OilTemperature",
                                        "GP3_Position", "GP3_Velocity", "GP3_PushPressure", "GP3_PressureA",
                                        "GP3_PressureB", "GP3_ClaspPressure", "GP3_OilTemperature", "GP4_Position",
                                        "GP4_Velocity", "GP4_PushPressure", "GP4_PressureA", "GP4_PressureB",
                                        "GP4_ClaspPressure", "GP4_OilTemperature", "OutsideTemp", "Locatie",
                                        "TempTimestamp", "Tel"],
                        "Values":
                            self.ya
                    }, },
            "GlobalParameters": {
            }
        }

        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/040cfdb467654f4f9cde4de093f006f8/services/f4b1cb042dbd412888016ba2ea357a2c/execute?api-version=2.0&details=true'
        api_key = 'fAchtI/DrjJwzVpuliCngwQNULV2gPWwRgAOFX65/2iGamHWbT0C6k0IDebX3hL65KAdr1cjChBVdkJK15GpsA=='  # Replace this with the API key for the web service
        headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

        # req = urllib.Request(url, body, headers)

        try:
            # response = urllib.urlopen(req)

            # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
            req = urllib.request.Request(url, body, headers)
            response = urllib.request.urlopen(req)
            json_response = json.loads(response.read())
            values = json_response["Results"]["output1"]["value"]["Values"]
            totaal = 0
            for i in values:
                totaal += float(i[0])
            totaal = totaal / len(values)

            return totaal

        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))
