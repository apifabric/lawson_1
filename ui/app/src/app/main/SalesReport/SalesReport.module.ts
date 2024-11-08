import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SALESREPORT_MODULE_DECLARATIONS, SalesReportRoutingModule} from  './SalesReport-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    SalesReportRoutingModule
  ],
  declarations: SALESREPORT_MODULE_DECLARATIONS,
  exports: SALESREPORT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class SalesReportModule { }