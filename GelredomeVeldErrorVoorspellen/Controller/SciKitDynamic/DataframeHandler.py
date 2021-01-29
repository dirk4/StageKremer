from Controller.SciKitDynamic.DynamicCsvConverter import DynamicCsvConverter
import pandas as pd
import pickle


class DataframeHandler:
    dataframe = pd.read_csv('Recources\\Volledige_Gelredome_Data_CSV.csv', index_col=False)

    def load_dataframe(self, location, part, time, value_type):
        csvConverter = DynamicCsvConverter(location, part, time, value_type,
                                           self.dataframe)
        df = csvConverter.make_file()
        df = df.drop(columns=['Timestamp'])
        return df.dropna()

    def save_dataframe(self, locatie):
        pickle.dump(self.dataframe, locatie)

