import os
import zipfile
from os import walk
import pandas as pd
from os import walk

url = 'C:\\Users\\Lukassen\\Desktop\\Stage\\Dataset v2\\zipped'
extracted_url = 'C:\\Users\\Lukassen\\Desktop\\Stage\\Dataset v2\\zipped\\extracted'

files = []
for (dirpath, dirnames, filenames) in walk(url):
    files.extend(filenames)
    break

for i in files:
    zip = zipfile.ZipFile(url + '\\' + i)
    zip.extractall(extracted_url)

print('All files are extraced')
print('Start of removing unneceserry files')


for fname in os.listdir(extracted_url):
    if not fname.startswith("KremerDataLog_"):
        os.remove(os.path.join(extracted_url, fname))


print('start combining files')

extracted_files = []
for (dirpath, dirnames, filenames) in walk(extracted_url):
    extracted_files.extend(filenames)
    break

startfile = 'C:\\Users\\Lukassen\\Desktop\\Stage\\Dataset v2\\KremerDataLog_start.csv'
full_csv = pd.read_csv(startfile, sep=';')


for i in extracted_files:
    url = extracted_url + '\\' + i

    try:
        csv = pd.read_csv(url, sep=';')
        full_csv = full_csv.append(csv)
    except:
        print('file ' + url + ' went wrong')

print('start sorting csv')
print(full_csv.columns)
full_csv = full_csv.sort_values('Timestamp')
full_csv = full_csv.reindex()
print(full_csv)
full_csv.to_csv('C:\\Users\\Lukassen\\Desktop\\Stage\\Dataset v2\\KremerDataLog_Full.csv')
print('WE DONE')

