import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http'

@Component({
  selector: 'app-train-sci-kit',
  templateUrl: './train-sci-kit.component.html',
  styleUrls: ['./train-sci-kit.component.css']
})
export class TrainSciKitComponent implements OnInit {


  constructor(private http: HttpClient) {
  }

  ngOnInit() {
  }

  trainingConformation() {
      return window.confirm('Are you sure you want to retrain the model. This could mess up the model')
  }

  startTraining() {
    var start = performance.now()
    this.http.get('http://localhost:8000/trainSci').subscribe(result =>{
      console.log(result);
      console.log(performance.now() - start)
  })
  }
}
