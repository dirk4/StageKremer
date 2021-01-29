from django.contrib import admin
from django.urls import path
from Django import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphLoad/', views.graph_load, name='graphload'),
    path('trainDynamicSciKit/', views.train_dynamic_scikit, name='trainDynamicSciKit'),
    path('trainTensor/', views.train_tensor, name='trainTensor'),
    path('predictAzure/<int:num>', views.predict_azure, name='predictAzure'),
    path('predictTensor/<int:num>', views.predict_tensor, name='predictTensor'),
    path('trainSci/', views.train_sci_kit, name='trainSciKit'),
    path('predictSci/<int:num>', views.predict_sci_kit, name='predictTensor'),
    path('trainSciPeaks/<int:num>/<str:location>', views.train_sci_kit_peaks, name='trainPeaks'),
    path('trainModel/', views.train_model, name='trainModel'),
    path('predictModel/', views.predict_model, name='predictModel'),
    path('cleanJson/', views.clean_json, name='cleanJson')
]
