import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainTensorflowComponent } from './train-tensorflow.component';

describe('TrainTensorflowComponent', () => {
  let component: TrainTensorflowComponent;
  let fixture: ComponentFixture<TrainTensorflowComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TrainTensorflowComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainTensorflowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
