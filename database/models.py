# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 08, 2024 05:42:50
# Database: sqlite:////tmp/tmp.mzoRsGnlVq/lawson_1/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Category(SAFRSBaseX, Base):
    """
    description: Represents product categories to which products belong.
    """
    __tablename__ = 'category'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductCategoryList : Mapped[List["ProductCategory"]] = relationship(back_populates="category")



class Customer(SAFRSBaseX, Base):
    """
    description: Represents a customer with personal and contact information.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    balance = Column(Float)
    credit_limit = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")



class Department(SAFRSBaseX, Base):
    """
    description: Contains information about company departments.
    """
    __tablename__ = 'department'
    _s_collection_name = 'Department'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    EmployeeDepartmentList : Mapped[List["EmployeeDepartment"]] = relationship(back_populates="department")



class Employee(SAFRSBaseX, Base):
    """
    description: Represents employees working in the organization.
    """
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    EmployeeDepartmentList : Mapped[List["EmployeeDepartment"]] = relationship(back_populates="employee")



class Product(SAFRSBaseX, Base):
    """
    description: Contains information about products available for purchase.
    """
    __tablename__ = 'product'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit_price = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="product")
    ProductCategoryList : Mapped[List["ProductCategory"]] = relationship(back_populates="product")
    ItemList : Mapped[List["Item"]] = relationship(back_populates="product")



class Supplier(SAFRSBaseX, Base):
    """
    description: Represents suppliers who provide products.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="supplier")



class EmployeeDepartment(SAFRSBaseX, Base):
    """
    description: Junction table for many-to-many relationship between employees and departments.
    """
    __tablename__ = 'employee_department'
    _s_collection_name = 'EmployeeDepartment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    employee_id = Column(ForeignKey('employee.id'), nullable=False)
    department_id = Column(ForeignKey('department.id'), nullable=False)

    # parent relationships (access parent)
    department : Mapped["Department"] = relationship(back_populates=("EmployeeDepartmentList"))
    employee : Mapped["Employee"] = relationship(back_populates=("EmployeeDepartmentList"))

    # child relationships (access children)



class Inventory(SAFRSBaseX, Base):
    """
    description: Tracks product stocks in inventory.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    supplier_id = Column(ForeignKey('supplier.id'), nullable=False)
    stock_quantity = Column(Integer)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("InventoryList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Represents an order placed by a customer, including order details.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False)
    date_shipped = Column(DateTime)
    amount_total = Column(Float)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    ItemList : Mapped[List["Item"]] = relationship(back_populates="order")
    SalesReportList : Mapped[List["SalesReport"]] = relationship(back_populates="order")



class ProductCategory(SAFRSBaseX, Base):
    """
    description: Junction table for many-to-many relationship between products and categories.
    """
    __tablename__ = 'product_category'
    _s_collection_name = 'ProductCategory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    category_id = Column(ForeignKey('category.id'), nullable=False)

    # parent relationships (access parent)
    category : Mapped["Category"] = relationship(back_populates=("ProductCategoryList"))
    product : Mapped["Product"] = relationship(back_populates=("ProductCategoryList"))

    # child relationships (access children)



class Item(SAFRSBaseX, Base):
    """
    description: Represents individual line items within an order.
    """
    __tablename__ = 'item'
    _s_collection_name = 'Item'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'), nullable=False)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    amount = Column(Float)
    unit_price = Column(Float, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("ItemList"))
    product : Mapped["Product"] = relationship(back_populates=("ItemList"))

    # child relationships (access children)



class SalesReport(SAFRSBaseX, Base):
    """
    description: Represents sales report data.
    """
    __tablename__ = 'sales_report'
    _s_collection_name = 'SalesReport'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'), nullable=False)
    report_date = Column(DateTime)
    total_sales = Column(Float)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("SalesReportList"))

    # child relationships (access children)
