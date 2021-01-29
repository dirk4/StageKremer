import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChartMakerComponent } from './chart-maker.component';

describe('ChartMakerComponent', () => {
  let component: ChartMakerComponent;
  let fixture: ComponentFixture<ChartMakerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChartMakerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChartMakerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
