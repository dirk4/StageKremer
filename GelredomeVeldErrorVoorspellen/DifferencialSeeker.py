import matplotlib.pyplot as plt
import pandas as pd
from Controller.TempFinalPackage.NewPredictor import Predictor

amount = 200
predictor = Predictor()
csv: pd.DataFrame = predictor.predictor('peak', 1, 'ClaspPressure', 5)
csv2: pd.DataFrame = predictor.predictor('peak', 1, 'ClaspPressure', 10)
csv = csv.sort_index()
csv2 = csv2.sort_index()
csv = csv.merge(csv2, left_index=True, right_index=True).drop(columns='actual_y')
if amount > csv.size:
    amount = csv.size
print(csv.columns)
print(csv)

peaks_actual = csv['actual_x'].head(amount).tolist()
peaks_predict5 = csv['prediction_x'].head(amount).tolist()
peaks_predict10 = csv['prediction_y'].head(amount).tolist()


def danger_checker(values: []):
    positives = 0
    negatives = 0
    for i in values:
        if i < 0:
            negatives += 1
        elif i > 0:
            positives += 1
    if negatives == len(values) or positives == len(values):
        return True
    else:
        return False


def percentage_maker(values):
    increases = []
    for i in range(10, len(values)):

        current = []
        future = []
        for j in range(1, 10):
            current.append(values[i - j])
        for j in range(0, 5):
            future.append(values[i - j])
        current_avarage = sum(current) / len(current)
        future_avarage = sum(future) / len(future)
        increase = ((future_avarage - current_avarage) / current_avarage) * 100
        increases.append(increase)
    return increases


# print(peaks)
hl, = plt.plot([], [])
plt.ion()

# plt.figure()
actual_increase_percentage = percentage_maker(peaks_actual)
predict_increase_percentage = percentage_maker(peaks_predict5)
print(actual_increase_percentage)
print(predict_increase_percentage)

for i in range(0, int(amount / 2)):
    plt.clf()
    actual_relevant = []
    predict5_releveant = []
    predict10_releveant = []

    for j in reversed(range(0, int(amount / 2))):
        actual_relevant.append(peaks_actual[i - j])
        predict5_releveant.append(peaks_predict5[i - j])
        predict10_releveant.append(peaks_predict10[i - j])
    plt.plot(actual_relevant, label='actual')
    plt.plot(predict5_releveant, label='prediction5')
    plt.plot(predict10_releveant, label='prediction10')
    plt.legend()
    plt.show()
    plt.draw()
    plt.pause(0.01)

    if danger_checker(actual_increase_percentage[8:-i]):
        print(actual_increase_percentage[8:-i])
        plt.pause(10)
        raise Exception('Trend going upward/downward')

print('We done over here e')
