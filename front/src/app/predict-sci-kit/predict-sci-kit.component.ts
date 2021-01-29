import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-predict-sci-kit',
  templateUrl: './predict-sci-kit.component.html',
  styleUrls: ['./predict-sci-kit.component.css']
})
export class PredictSciKitComponent implements OnInit {

  url = 'http://localhost:8000/predictSci/'
  constructor(private http: HttpClient) { }


  ngOnInit() {
    console.log('PredictTensorflowComponent has been called (ngOnInit)')
  }

  async getPrediction(number: number) {
    console.log('PredictAzureComponent has been called (getPrediction)')
    return await this.http.get<string>(this.url + number).toPromise()
  }

}
