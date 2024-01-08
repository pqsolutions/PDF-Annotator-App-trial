import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PdfRoutingModule } from './pdf-routing.module';
import { PdfMasterComponent } from './pdf-master/pdf-master.component';
import { AnnotatorComponent } from './annotator/annotator.component';
import { FileListComponent } from './file-list/file-list.component';
import { TransactionsComponent } from './transactions/transactions.component';
import { SharedModule } from '../shared/shared.module';
import { PqUiModule } from '@pq/pq-ui';
import { NgxExtendedPdfViewerModule } from 'ngx-extended-pdf-viewer';

@NgModule({
  declarations: [
    PdfMasterComponent,
    AnnotatorComponent,
    FileListComponent,
    TransactionsComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
    PqUiModule,
    NgxExtendedPdfViewerModule,
    PdfRoutingModule
  ]
})
export class PdfModule { }
