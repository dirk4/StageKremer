import pandas as pd

df = pd.read_csv('Recources\\Volledige_Gelredome_Data_CSV.csv')

json_str = '['

for i in range(0, int(len(df)/5)):
    json_str = json_str + '''{
    "gripperjack": 1,
    "part": "ClaspPressure",
    "type": "peak",
    "data":'''

    json_str = json_str + df.loc[i].to_json()
    json_str = json_str + '}'
    if float(i) is not (len(df)/5):
        json_str = json_str + ','

json_str = json_str + ']'
print(json_str)


text_file = open("jsonText.txt", "w")
n = text_file.write(json_str)
text_file.close()
