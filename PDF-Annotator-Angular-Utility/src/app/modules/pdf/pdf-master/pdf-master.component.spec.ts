import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PdfMasterComponent } from './pdf-master.component';

describe('PdfMasterComponent', () => {
  let component: PdfMasterComponent;
  let fixture: ComponentFixture<PdfMasterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PdfMasterComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PdfMasterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
