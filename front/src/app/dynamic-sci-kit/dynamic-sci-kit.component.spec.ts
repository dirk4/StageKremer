import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DynamicSciKitComponent } from './dynamic-sci-kit.component';

describe('DynamicSciKitComponent', () => {
  let component: DynamicSciKitComponent;
  let fixture: ComponentFixture<DynamicSciKitComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DynamicSciKitComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DynamicSciKitComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
