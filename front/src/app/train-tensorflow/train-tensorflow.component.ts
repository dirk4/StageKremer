import { Component, Injectable, OnInit } from '@angular/core';

import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-train-tensorflow',
  templateUrl: './train-tensorflow.component.html',
  styleUrls: ['./train-tensorflow.component.css']
})
export class TrainTensorflowComponent implements OnInit {

  constructor(private http: HttpClient) {
  }

  ngOnInit() {
  }

  trainingConformation() {
      return window.confirm('Are you sure you want to retrain the model. This could mess up the model')
  }

  startTraining() {
    var start = performance.now()
    this.http.get('http://localhost:8000/trainTensor').subscribe(result => {
      // console.log(result);
      console.log(performance.now() - start)
    })
  }
}
@Component({
  selector: 'dialog-content-example-dialog',
  templateUrl: 'train-tensorflow-dialog.html',
})
export class DialogContentExampleDialog { }