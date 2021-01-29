import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowPredictionGraphComponent } from './show-prediction-graph.component';

describe('ShowPredictionGraphComponent', () => {
  let component: ShowPredictionGraphComponent;
  let fixture: ComponentFixture<ShowPredictionGraphComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ShowPredictionGraphComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ShowPredictionGraphComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
