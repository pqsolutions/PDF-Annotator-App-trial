import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PdfMasterComponent } from './modules/pdf/pdf-master/pdf-master.component';

const routes: Routes = [
  { path: '', redirectTo: 'pdf', pathMatch: 'full' },
  { 
    path: 'pdf', component: PdfMasterComponent,
    loadChildren: () => import('./modules/pdf/pdf.module').then(m => m.PdfModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
