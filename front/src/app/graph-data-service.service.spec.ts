import { TestBed } from '@angular/core/testing';

import { GraphDataServiceService } from './graph-data-service.service';

describe('GraphDataServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: GraphDataServiceService = TestBed.get(GraphDataServiceService);
    expect(service).toBeTruthy();
  });
});
