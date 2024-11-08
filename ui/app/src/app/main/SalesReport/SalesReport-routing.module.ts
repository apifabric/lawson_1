import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SalesReportHomeComponent } from './home/SalesReport-home.component';
import { SalesReportNewComponent } from './new/SalesReport-new.component';
import { SalesReportDetailComponent } from './detail/SalesReport-detail.component';

const routes: Routes = [
  {path: '', component: SalesReportHomeComponent},
  { path: 'new', component: SalesReportNewComponent },
  { path: ':id', component: SalesReportDetailComponent,
    data: {
      oPermission: {
        permissionId: 'SalesReport-detail-permissions'
      }
    }
  }
];

export const SALESREPORT_MODULE_DECLARATIONS = [
    SalesReportHomeComponent,
    SalesReportNewComponent,
    SalesReportDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SalesReportRoutingModule { }