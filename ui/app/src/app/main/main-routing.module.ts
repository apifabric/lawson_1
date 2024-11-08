import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Category', loadChildren: () => import('./Category/Category.module').then(m => m.CategoryModule) },
    
        { path: 'Customer', loadChildren: () => import('./Customer/Customer.module').then(m => m.CustomerModule) },
    
        { path: 'Department', loadChildren: () => import('./Department/Department.module').then(m => m.DepartmentModule) },
    
        { path: 'Employee', loadChildren: () => import('./Employee/Employee.module').then(m => m.EmployeeModule) },
    
        { path: 'EmployeeDepartment', loadChildren: () => import('./EmployeeDepartment/EmployeeDepartment.module').then(m => m.EmployeeDepartmentModule) },
    
        { path: 'Inventory', loadChildren: () => import('./Inventory/Inventory.module').then(m => m.InventoryModule) },
    
        { path: 'Item', loadChildren: () => import('./Item/Item.module').then(m => m.ItemModule) },
    
        { path: 'Order', loadChildren: () => import('./Order/Order.module').then(m => m.OrderModule) },
    
        { path: 'Product', loadChildren: () => import('./Product/Product.module').then(m => m.ProductModule) },
    
        { path: 'ProductCategory', loadChildren: () => import('./ProductCategory/ProductCategory.module').then(m => m.ProductCategoryModule) },
    
        { path: 'SalesReport', loadChildren: () => import('./SalesReport/SalesReport.module').then(m => m.SalesReportModule) },
    
        { path: 'Supplier', loadChildren: () => import('./Supplier/Supplier.module').then(m => m.SupplierModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }