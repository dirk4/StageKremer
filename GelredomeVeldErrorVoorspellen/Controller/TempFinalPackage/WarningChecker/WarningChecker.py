import pandas as pd
import Controller.TempFinalPackage.WarningChecker.partWarnings as pw
import json
import numpy as np

# Types of warnings

# -to big difference of avarage
# -to many followed up increases/decreases
# -value gets over warning value


def check_all(dataframe, part):
    all_values = np.load('C:\\Users\\Lukassen\\PycharmProjects\\GelredomeVeldErrorVoorspellen\\Recources\\lastValues.npy')
    part_checker = pw.part_warnings_factory(part)
    print(len(all_values))
    print(all_values)
    print('NasiBami')
    if len(all_values) > 4:

        return '{ "avarage": "' + str(check_avarage(dataframe[0])) + '",' \
                                                                     '"increases": "' + str(
            check_increases(all_values)) + '",' \
                                           '"decreases": "' + str(check_decreases(all_values)) + '", '\
                '"part": "' + str(part_checker.warning_checker(dataframe)) + '"}'
    else:
        return '{ "avarage": "False",' \
               '"increases": "False",' \
               '"decreases": "Fasle", ' \
               '"part": "' + str(part_checker.warning_checker(dataframe)) + '"}'

        pass


def check_avarage(df):
    all_values = np.load('C:\\Users\\Lukassen\\PycharmProjects\\GelredomeVeldErrorVoorspellen\\Recources\\lastValues.npy')

    last_values = all_values[-5:]
    print(last_values)

    diff = max(last_values) - min(last_values)

    avg = sum(last_values) / len(last_values)
    print(avg)
    print(df)
    if not (avg + diff * 0.30 > df > avg - diff * 0.30):
        return True
    else:
        return False


def check_increases(df: pd.DataFrame):
    increases = 0
    print(df)
    print('AAAAAAAA')
    total =0
    for i in range(len(df) - 5, len(df)):
        total = total+1
        if df[i] > df[i - 1]:
            increases += 1
        else:
            increases = 0
    print(total)
    print('TotalCounterCheck')
    if increases == 5:
        return True
        pass
    return False
    pass


def check_decreases(df: pd.DataFrame):
    decreases = 0
    print(df)
    for i in range(len(df) - 5, len(df)):
        if df[i] < df[i - 1]:
            decreases += 1
        else:
            decreases = 0

        if decreases == 5:
            return True
        pass
    return False
    pass
