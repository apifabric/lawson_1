# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Customer(Base):
    """
    description: Represents a customer with personal and contact information.
    """
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    balance = Column(Float, default=0.0)
    credit_limit = Column(Float, default=1000.0)


class Order(Base):
    """
    description: Represents an order placed by a customer, including order details.
    """
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    date_shipped = Column(DateTime, nullable=True)
    amount_total = Column(Float, default=0.0)


class Product(Base):
    """
    description: Contains information about products available for purchase.
    """
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    unit_price = Column(Float, nullable=False)


class Item(Base):
    """
    description: Represents individual line items within an order.
    """
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    amount = Column(Float, default=0.0)
    unit_price = Column(Float, nullable=False)


class Supplier(Base):
    """
    description: Represents suppliers who provide products.
    """
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_email = Column(String, nullable=True)


class Inventory(Base):
    """
    description: Tracks product stocks in inventory.
    """
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('supplier.id'), nullable=False)
    stock_quantity = Column(Integer, default=0)


class Category(Base):
    """
    description: Represents product categories to which products belong.
    """
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


class ProductCategory(Base):
    """
    description: Junction table for many-to-many relationship between products and categories.
    """
    __tablename__ = 'product_category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)


class Employee(Base):
    """
    description: Represents employees working in the organization.
    """
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)


class Department(Base):
    """
    description: Contains information about company departments.
    """
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


class EmployeeDepartment(Base):
    """
    description: Junction table for many-to-many relationship between employees and departments.
    """
    __tablename__ = 'employee_department'
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)


class SalesReport(Base):
    """
    description: Represents sales report data.
    """
    __tablename__ = 'sales_report'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    report_date = Column(DateTime, default=datetime.datetime.utcnow)
    total_sales = Column(Float, default=0.0)


# Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')

# Create tables in the database
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Populate sample data
customer1 = Customer(name="John Doe", email="john.doe@example.com", balance=500.0)
customer2 = Customer(name="Jane Smith", email="jane.smith@example.com", balance=1500.0)

product1 = Product(name="Widget", unit_price=20.0)
product2 = Product(name="Gadget", unit_price=50.0)

order1 = Order(customer_id=1, amount_total=400.0)
order2 = Order(customer_id=2, date_shipped=datetime.datetime(2023, 10, 1), amount_total=300.0)

item1 = Item(order_id=1, product_id=1, quantity=20, amount=400.0, unit_price=20.0)
item2 = Item(order_id=2, product_id=2, quantity=6, amount=300.0, unit_price=50.0)

supplier1 = Supplier(name="Acme Corp", contact_email="supply@acme.com")
supplier2 = Supplier(name="Globex Inc", contact_email="info@globex.com")

inventory1 = Inventory(product_id=1, supplier_id=1, stock_quantity=100)
inventory2 = Inventory(product_id=2, supplier_id=2, stock_quantity=200)

category1 = Category(name="Electronics")
category2 = Category(name="Household")

product_category1 = ProductCategory(product_id=1, category_id=1)
product_category2 = ProductCategory(product_id=2, category_id=2)

employee1 = Employee(name="Alice Johnson", position="Manager")
employee2 = Employee(name="Bob Brown", position="Salesperson")

department1 = Department(name="Sales")
department2 = Department(name="Customer Service")

employee_department1 = EmployeeDepartment(employee_id=1, department_id=1)
employee_department2 = EmployeeDepartment(employee_id=2, department_id=2)

sales_report1 = SalesReport(order_id=1, total_sales=400.0)
sales_report2 = SalesReport(order_id=2, total_sales=300.0)

session.add_all([
    customer1, customer2, product1, product2, order1, order2, item1, item2,
    supplier1, supplier2, inventory1, inventory2, category1, category2, product_category1,
    product_category2, employee1, employee2, department1, department2, employee_department1,
    employee_department2, sales_report1, sales_report2
])

session.commit()
session.close()
