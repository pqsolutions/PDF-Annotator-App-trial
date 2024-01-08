import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AnnotatorComponent } from './annotator/annotator.component';

const routes: Routes = [
  { path: '', redirectTo: 'annotator', pathMatch: 'full' },
  { path: 'annotator', component: AnnotatorComponent }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PdfRoutingModule { }
