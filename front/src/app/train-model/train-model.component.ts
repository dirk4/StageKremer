import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-train-model',
  templateUrl: './train-model.component.html',
  styleUrls: ['./train-model.component.css']
})
export class TrainModelComponent implements OnInit {

  url = 'http://127.0.0.1:8000/trainModel/'
  contactForm: FormGroup;
  going = true
  mae = ''
  mape = ''


  gripperjacks = [
    { id: 1, name: 1 },
    { id: 2, name: 2 },
    { id: 3, name: 3 },
    { id: 4, name: 4 }
  ];

  parts = [
    { id: "Velocity", name: "Velocity" },
    { id: "PushPressure", name: "PushPressure" },
    { id: "PressureA", name: "PressureA" },
    { id: "PressureB", name: "PressureB" },
    { id: "ClaspPressure", name: "ClaspPressure" },
    { id: "OilTemperature", name: "OilTemperature" },
  ]
  
  return_types = [
    { id: "peak", name: "peak" },
    { id: "low", name: "low" },
    { id: "middle_peak", name: "middle_peak" },
    { id: "middle_low", name: "middle_low" },
  ]

  time_frames = [
    { id: "1min", name: "1min" },
    { id: "5min", name: "5min" },
    { id: "10min", name: "10min" },
  ]


  jsonStringMaker(gripperjack, part){
    return '{     "gripperjack": "'+ gripperjack + '",  "part": "'+ part + '",     "interval": "5 min",     "return_type": "peak" }'
  }

  requestSender(gripperjackIndex, partIndex){
    if (!this.going){
      return null
    }
    console.log('Requestsender has activated')
    console.log(this.gripperjacks[1]['id'])
    var json = this.jsonStringMaker(this.gripperjacks[gripperjackIndex]['id'], this.parts[partIndex]['id'])

    console.log(json)
    this.http.post(this.url, json).subscribe(data=> {
      console.log('Current gripperjack = ' + this.gripperjacks[gripperjackIndex])
      console.log('Current part = '+ this.parts[partIndex])
      if(gripperjackIndex == 3 && partIndex == 5){
        console.log('END')
        this.stopRequest()
        return null
      }
      else if(partIndex == 5){
        return this.requestSender(gripperjackIndex + 1, 0)
      }
      else{
        return this.requestSender(gripperjackIndex, partIndex + 1)
      }
    })
  }

  constructor(private fb: FormBuilder, private http: HttpClient) { }

  startRequest(){
    this.going = true
    this.requestSender(0,0)
  }
  stopRequest(){
    this.going = false
  }


  ngOnInit() {
    console.log('TrainModelComponent has been called')
    this.contactForm = this.fb.group({
      gripperjack: [this.gripperjacks[0]['name']],
      part: [this.parts[0]['name']],
      return_type: [this.return_types[0]['name']],
      time_interval: [this.time_frames[0]['name']]
    });
  }


  train(){
    this.mae = 'calculating...'
    this.mape = 'calculating...'

    console.log(this.contactForm.value)
    console.log(this.contactForm)
    this.http.post('http://localhost:8000/trainModel/', this.contactForm.value).subscribe(data => {
      this.mae = data[0];
      this.mape = data[1];
        })
  }

  submit(button: string) {
    if(button == 'train'){
      this.train()
    }
  }
    // Update values when they get changed
    changeGripperjack(e) {
      this.contactForm.value['gripperjack'] = e.target.value
    }
    changePart(e) {
      this.contactForm.value['part'] = e.target.value
    }
    changeValueType(e) {
      this.contactForm.value['return_type'] = e.target.value
    }
    changeTimeInterval(e) {
      this.contactForm.value['time_interval'] = e.target.value
    }

}
