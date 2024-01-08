import { Injectable } from '@angular/core';
import { DataService } from '../network/data.service';

@Injectable({
  providedIn: 'root'
})
export class AnnotationService {

  constructor(
    private dataService: DataService
  ) { }

  getPDF() {
    return this.dataService.doGetPDF('sample-invoice');
  }
}
