import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import {MatProgressSpinnerModule} from '@angular/material';


@Component({
  selector: 'app-predict-azure',
  templateUrl: './predict-azure.component.html',
  styleUrls: ['./predict-azure.component.css']
})
export class PredictAzureComponent implements OnInit {
  url = 'http://localhost:8000/predictAzure/'
  spinner = MatProgressSpinnerModule
  constructor(private http: HttpClient) { }

  ngOnInit() {
    console.log('PredictAzureComponent has been called (ngOnInit)')
  }

  async getPrediction(number: number) {
    console.log('PredictAzureComponent has been called (getPrediction)')
    return await this.http.get<string>(this.url + number).toPromise()
  }
}
