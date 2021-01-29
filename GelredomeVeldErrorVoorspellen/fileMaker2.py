import os
import zipfile
from os import walk
import pandas as pd
from os import walk
from tkinter import Tcl

url = 'C:\\Users\\Lukassen\\Desktop\\Stage\\Dataset v2\\zipped\\AlarmLog'

files = []
for (dirpath, dirnames, filenames) in walk(url):
    print(dirpath)
    print(dirnames)
    print(filenames)
    files.extend(filenames)
    break

df = []
for f in files:
    try:
        df.append(pd.read_csv(url + '\\' + f, sep=';'))
        print('file went correct: ' +  url + '\\' + f)
    except:
        print('something went wrong on file: ' + url + '\\' + f)

full_df = pd.concat(df)
print(full_df)
