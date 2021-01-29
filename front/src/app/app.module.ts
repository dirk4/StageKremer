import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PredictTensorflowComponent } from './predict-tensorflow/predict-tensorflow.component';
import { PredictAzureComponent } from './predict-azure/predict-azure.component';
import { TrainTensorflowComponent } from './train-tensorflow/train-tensorflow.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ReactiveFormsModule } from '@angular/forms';
import { ShowPredictionGraphComponent } from './show-prediction-graph/show-prediction-graph.component';
import { TrainSciKitComponent } from './train-sci-kit/train-sci-kit.component';
import { PredictSciKitComponent } from './predict-sci-kit/predict-sci-kit.component';
import { DynamicSciKitComponent } from './dynamic-sci-kit/dynamic-sci-kit.component';
import { FormsModule } from '@angular/forms';
import { ChartMakerComponent } from './chart-maker/chart-maker.component';
import { TrainModelComponent } from './train-model/train-model.component';
import { PredictModelComponent } from './predict-model/predict-model.component';
import { DataDashboardComponent } from './data-dashboard/data-dashboard.component'


@NgModule({
  declarations: [
    AppComponent,
    PredictTensorflowComponent,
    PredictAzureComponent,
    TrainTensorflowComponent,
    ShowPredictionGraphComponent,
    TrainSciKitComponent,
    PredictSciKitComponent,
    DynamicSciKitComponent,
    ChartMakerComponent,
    TrainModelComponent,
    PredictModelComponent,
    DataDashboardComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
