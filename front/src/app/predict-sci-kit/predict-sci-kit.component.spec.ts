import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PredictSciKitComponent } from './predict-sci-kit.component';

describe('PredictSciKitComponent', () => {
  let component: PredictSciKitComponent;
  let fixture: ComponentFixture<PredictSciKitComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PredictSciKitComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PredictSciKitComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
