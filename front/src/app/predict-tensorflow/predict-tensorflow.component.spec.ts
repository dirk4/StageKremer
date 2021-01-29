import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PredictTensorflowComponent } from './predict-tensorflow.component';

describe('PredictTensorflowComponent', () => {
  let component: PredictTensorflowComponent;
  let fixture: ComponentFixture<PredictTensorflowComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PredictTensorflowComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PredictTensorflowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
