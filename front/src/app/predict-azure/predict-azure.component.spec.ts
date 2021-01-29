import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PredictAzureComponent } from './predict-azure.component';

describe('PredictAzureComponent', () => {
  let component: PredictAzureComponent;
  let fixture: ComponentFixture<PredictAzureComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PredictAzureComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PredictAzureComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
