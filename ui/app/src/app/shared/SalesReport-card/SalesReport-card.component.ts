import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './SalesReport-card.component.html',
  styleUrls: ['./SalesReport-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.SalesReport-card]': 'true'
  }
})

export class SalesReportCardComponent {


}