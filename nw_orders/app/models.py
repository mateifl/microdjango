from django.db import models


class Customer(models.Model):
    customerid = models.CharField(db_column='CustomerID', primary_key=True, max_length=5)
    company_name = models.CharField(db_column='CompanyName', max_length=40)
    contact_name = models.CharField(db_column='ContactName', max_length=30)
    contact_title = models.CharField(db_column='ContactTitle', max_length=30)
    address = models.CharField(db_column='Address', max_length=60)
    city = models.CharField(db_column='City', max_length=15)
    region = models.CharField(db_column='Region', max_length=15)
    postal_code = models.CharField(db_column='PostalCode', max_length=10)
    country = models.CharField(db_column='Country', max_length=15)
    phone = models.CharField(db_column='Phone', max_length=24)
    fax = models.CharField(db_column='Fax', max_length=24)

    class Meta:
        db_table = 'customers'


class Employee(models.Model):
    employeeid = models.AutoField(db_column='EmployeeID', primary_key=True)
    last_name = models.CharField(db_column='LastName', max_length=20)
    first_name = models.CharField(db_column='FirstName', max_length=10)
    title = models.CharField(db_column='Title', max_length=30)
    title_of_courtesy = models.CharField(db_column='TitleOfCourtesy', max_length=25)
    birth_date = models.DateTimeField(db_column='BirthDate')
    hire_date = models.DateTimeField(db_column='HireDate')
    address = models.CharField(db_column='Address', max_length=60)
    city = models.CharField(db_column='City', max_length=15)
    region = models.CharField(db_column='Region', max_length=15)
    postal_code = models.CharField(db_column='PostalCode', max_length=10)
    country = models.CharField(db_column='Country', max_length=15)
    home_phone = models.CharField(db_column='HomePhone', max_length=24)
    extension = models.CharField(db_column='Extension', max_length=4)
    photo = models.CharField(db_column='Photo', max_length=50)
    notes = models.TextField(db_column='Notes', blank=True, null=True)
    reports_to = models.ForeignKey('self', models.DO_NOTHING, db_column='ReportsTo', blank=True, null=True)

    class Meta:
        db_table = 'employees'


class Shippers(models.Model):
    shipperid = models.AutoField(db_column='ShipperID', primary_key=True)
    company_name = models.CharField(db_column='CompanyName', max_length=40)
    phone = models.CharField(db_column='Phone', max_length=24)

    class Meta:
        db_table = 'shippers'


class Order(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustomerID')
    employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmployeeID')
    order_date = models.DateTimeField(db_column='OrderDate')
    required_date = models.DateTimeField(db_column='RequiredDate', blank=True, null=True)
    shipped_date = models.DateTimeField(db_column='ShippedDate', blank=True, null=True)
    shipvia = models.ForeignKey(Shippers, models.DO_NOTHING, db_column='ShipVia')
    freight = models.FloatField(db_column='Freight')
    ship_name = models.CharField(db_column='ShipName', max_length=40)
    ship_address = models.CharField(db_column='ShipAddress', max_length=60)
    ship_city = models.CharField(db_column='ShipCity', max_length=15)
    ship_region = models.CharField(db_column='ShipRegion', max_length=15)
    ship_postal_code = models.CharField(db_column='ShipPostalCode', max_length=10)
    ship_country = models.CharField(db_column='ShipCountry', max_length=15)

    class Meta:
        db_table = 'orders'


class OrderDetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    order = models.ForeignKey(Order, models.DO_NOTHING, db_column='OrderID')
    unit_price = models.FloatField(db_column='UnitPrice')
    quantity = models.PositiveSmallIntegerField(db_column='Quantity')
    discount = models.FloatField(db_column='Discount')
    product_id = models.IntegerField(db_column="ProductID")

    class Meta:
        db_table = 'order_details'
