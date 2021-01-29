import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainSciKitComponent } from './train-sci-kit.component';

describe('TrainSciKitComponent', () => {
  let component: TrainSciKitComponent;
  let fixture: ComponentFixture<TrainSciKitComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TrainSciKitComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainSciKitComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
