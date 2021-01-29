import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'
@Component({
  selector: 'app-predict-tensorflow',
  templateUrl: './predict-tensorflow.component.html',
  styleUrls: ['./predict-tensorflow.component.css']
})
export class PredictTensorflowComponent implements OnInit {

  url = 'http://localhost:8000/predictTensor/'
  constructor(private http: HttpClient) { }


  ngOnInit() {
    console.log('PredictTensorflowComponent has been called (ngOnInit)')
  }

  async getPrediction(number: number) {
    console.log('PredictAzureComponent has been called (getPrediction)')
    return await this.http.get<string>(this.url + number).toPromise()
  }
}
