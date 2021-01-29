import { HttpClient } from '@angular/common/http';
import { Component, ViewChild, OnInit } from '@angular/core';
import { NgForm, FormGroup, FormControl, FormBuilder } from '@angular/forms';
import { } from 'angular-nvd3'
import { GraphDataServiceService} from 'src/app/graph-data-service.service'

@Component({
  selector: 'app-dynamic-sci-kit',
  templateUrl: './dynamic-sci-kit.component.html',
  styleUrls: ['./dynamic-sci-kit.component.css']
})
export class DynamicSciKitComponent implements OnInit {

  title = 'Data trainer (AKA the gym)';
  contactForm: FormGroup;
  mae = ""
  mape = ""
  graphVisible = false;
  values;
  
  constructor(private fb: FormBuilder, private http: HttpClient, private graphDataService: GraphDataServiceService) {
    
  }

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
    { id: "avg", name: "avg" },
    { id: "min", name: "min" },
    { id: "max", name: "max" },
  ]

  time_frames = [
    { id: "1min", name: "1min" },
    { id: "5min", name: "5min" },
    { id: "10min", name: "10min" },
  ]

  ngOnInit() {
    this.contactForm = this.fb.group({
      gripperjack: [this.gripperjacks[0]['name']],
      part: [this.parts[0]['name']],
      return_type: [this.return_types[0]['name']],
      time_interval: [this.time_frames[0]['name']]
    });
  }


  train(){
    this.graphVisible = false
    this.mae = 'calculating...'
    this.mape = 'calculating...'

    console.log(this.contactForm.value)
    console.log(this.contactForm)
    this.http.post('http://localhost:8000/trainDynamicSciKit/', this.contactForm.value).subscribe(data => {
      this.mae = data[0];
      this.mape = data[1];
        })
    this.http.post('http://localhost:8000/graphLoad/', this.contactForm.value).subscribe(data => {
      this.graphDataService.data = data
      console.log(this.graphDataService.data)
    })
  }

  submit(button: string) {
    if(button == 'train'){
      this.train()
    }
    else if (button == 'graph'){
 
      this.showGraph()
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

  showGraph(){
    console.log('start showing the graph')
    this.graphVisible = true
  }
}

