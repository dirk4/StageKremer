from Controller.TempFinalPackage.NewPredictor import Predictor


def danger_checker_constant_raise(values: []):
    positives = 0
    negatives = 0

    for i in range(1, len(values)):
        if values[i] < values[i - 1]:
            negatives += 1
        elif values[i] > values[i - 1]:
            positives += 1

    if negatives == 0 or positives == 0:
        print(values)
        raise Exception('Constistent up/down ward trend')


def danger_checker_avarage(valuesfull: [], valueslast: []):
    avaragefull = sum(valuesfull) / len(valuesfull)
    avaragelast = sum(valueslast) / len(valueslast)
    if avaragelast > avaragefull * 1.25 or avaragelast < avaragefull * 0.75:
        raise Exception('To much difference from avarage')


predictor = Predictor()
last = list()
full = list()
for i in range(0, 20):
    print(i)
    prediction = predictor.predictor('peak', 1, 'ClaspPressure', '5min', i)[0]
    last.append(prediction)
    if len(last) > 6:
        last.pop(0)
        danger_checker_constant_raise(last)
        danger_checker_avarage(full)
    print(last)
