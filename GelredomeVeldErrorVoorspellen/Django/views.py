import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import pickle
import numpy as np


def index(request):
    return HttpResponse('')


@csrf_exempt
def train_dynamic_scikit(request):
    import Service.SciKitDynamicServiceTrain as skdst

    var = json.load(request)
    print(var)
    print(var['gripperjack'])
    print(var['part'])
    print(var['return_type'])
    print(var['time_interval'])
    gripperjack = str(var['gripperjack'])
    type = var['part']
    return_type = var['return_type']
    time_interval = var['time_interval']

    v = skdst.SciKitDynamicService(gripperjack, type, return_type, time_interval)
    accuracy = v.train_page_view()
    return HttpResponse(json.dumps(accuracy))


@csrf_exempt
def graph_load(request):
    import Service.SciKitDynamicServiceTrain as skdst

    var = json.load(request)
    print(var)
    print(var['gripperjack'])
    print(var['part'])
    print(var['return_type'])
    print(var['time_interval'])
    gripperjack = str(var['gripperjack'])
    type = var['part']
    return_type = var['return_type']
    time_interval = var['time_interval']

    v = skdst.SciKitDynamicService(gripperjack, type, return_type, time_interval)

    return HttpResponse(json.dumps(v.graph_info()))


def train_tensor(request):
    import Service.MLTrainServiceTensor as mlt

    ml = mlt.MLTrainService()
    return ml.train_page_view(request)


def predict_tensor(request, num):
    import Service.MLPredictServiceTensor as mlp

    ml = mlp.MLPredictService()
    return ml.predict_page_view(num)


def predict_azure(request, num):
    import Service.MLPredictServiceAzure as mla

    ml = mla.MLTrainService()
    return ml.predict_page_view(request, num)


def predict_sci_kit(request, num):
    import Service.MLPredictServiceSciKit as mlps

    ml = mlps.MLPredictServiceSciKit()
    return ml.predict_view_page(num)


def train_sci_kit(request):
    import Service.MLTrainServiceSciKit as mlts

    ml = mlts.MLTrainService()
    return ml.train_page_view()


def train_sci_kit_peaks(request, num, part):
    from Controller.TempFinalPackage import NewPredictor

    NewPredictor.predictor(num, part, -1)
    pass


@csrf_exempt
def train_model(request):
    from Service.TempFinalService.TrainService import TrainService

    var = json.load(request)
    print(var)

    trainer = TrainService(var['gripperjack'], var['part'], var['return_type'])
    mae = trainer.train()
    response_body = '{ "mae": ' + str(mae) + ' }'
    response: HttpResponse = HttpResponse(response_body)
    response.status_code = 200
    return response


@csrf_exempt
def predict_model(request):
    from Service.TempFinalService.PredictService import PredictService

    print('let get it')
    print(request)
    var = json.load(request)
    print(var)
    data_row = var['data']
    print(var['data'])
    t = PredictService(var['gripperjack'], var['part'], var['type'],
                       var['data'])
    prediction = t.predict()
    response: HttpResponse = HttpResponse()
    response.status_code = 200
    time = (datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime("%H:%M:%S")
    response_dict = '{"prediction": ' + str(prediction[0][0]) + ', "error": ' + prediction[1] + ',' \
                                                                                                '"time": "' + time + '"}'

    print(response_dict)

    response.write(response_dict)

    return response


def clean_json(request):
    np_array = []
    np.save('C:\\Users\\Lukassen\\PycharmProjects\\GelredomeVeldErrorVoorspellen\\Recources\\lastValues.npy', np_array)
    response: HttpResponse = HttpResponse()
    response.status_code = 200
    return response
