import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { PredictAzureComponent } from 'src/app/predict-azure/predict-azure.component'
import { PredictTensorflowComponent } from 'src/app/predict-tensorflow/predict-tensorflow.component'
import { TrainTensorflowComponent } from 'src/app/train-tensorflow/train-tensorflow.component'
import { TrainSciKitComponent } from 'src/app/train-sci-kit/train-sci-kit.component'
import { PredictSciKitComponent } from 'src/app/predict-sci-kit/predict-sci-kit.component'
import { FormControl } from '@angular/forms'
import { DynamicSciKitComponent } from 'src/app/dynamic-sci-kit/dynamic-sci-kit.component'
import { timer } from 'rxjs';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  predictionAzureComponent = new PredictAzureComponent(this.http)
  predictionTensorComponent = new PredictTensorflowComponent(this.http)
  trainTensorComponent = new TrainTensorflowComponent(this.http)
  predictSciKitComponent = new PredictSciKitComponent(this.http)
  trainSciKitComponent = new TrainSciKitComponent(this.http)

  constructor(private http: HttpClient) {
  }

  total = 0 
  prediction = ''
  number = new FormControl(0)
  time = 0
  
  predictAzure() {
    var timerStart = performance.now();
    if (this.number.value < 0 || this.number.value > 14) {
      this.prediction = 'CSV number is invalid'
    }
    else {
      this.prediction = 'Caluclating...'
      this.predictionAzureComponent.getPrediction(this.number.value).then(res => {this.prediction = res ; console.log(performance.now()- timerStart)})
    }
  }

  predictTensor() {
    var timerStart = performance.now();

    if (this.number.value < 0 || this.number.value > 14) {
      this.prediction = 'CSV number is invalid'
    }
    else {
      this.prediction = 'Calulating...'
      this.predictionTensorComponent.getPrediction(this.number.value).then(res =>  {this.prediction = res ; console.log(performance.now()- timerStart)});
    }
  }

  trainTensor() {

    if (this.trainTensorComponent.trainingConformation()) {
      this.prediction = 'Start training'
      this.trainTensorComponent.startTraining()
    }
  }

  predictSciKit(){
    var timerStart = performance.now();

    if (this.number.value < 0 || this.number.value > 14) {
      this.prediction = 'CSV number is invalid'
    }
    else {
      this.prediction = 'Calulating...'
      this.predictSciKitComponent.getPrediction(this.number.value).then(res =>  {this.prediction = res ; console.log(performance.now()- timerStart)});
    }
  }


  trainSciKit() {
    if (this.trainSciKitComponent.trainingConformation()) {
      this.prediction = 'Start training'
      this.trainSciKitComponent.startTraining()
    }
  }


}
