from django.db import models


class Customer(models.Model):
    customerid = models.CharField(db_column='CustomerID', primary_key=True, max_length=5)
    companyname = models.CharField(db_column='CompanyName', max_length=40)
    contactname = models.CharField(db_column='ContactName', max_length=30)
    contacttitle = models.CharField(db_column='ContactTitle', max_length=30)
    address = models.CharField(db_column='Address', max_length=60)
    city = models.CharField(db_column='City', max_length=15)
    region = models.CharField(db_column='Region', max_length=15)
    postalcode = models.CharField(db_column='PostalCode', max_length=10)
    country = models.CharField(db_column='Country', max_length=15)
    phone = models.CharField(db_column='Phone', max_length=24)
    fax = models.CharField(db_column='Fax', max_length=24)

    class Meta:
        db_table = 'customers'


class Employee(models.Model):
    employeeid = models.AutoField(db_column='EmployeeID', primary_key=True)
    lastname = models.CharField(db_column='LastName', max_length=20)
    firstname = models.CharField(db_column='FirstName', max_length=10)
    title = models.CharField(db_column='Title', max_length=30)
    titleofcourtesy = models.CharField(db_column='TitleOfCourtesy', max_length=25)
    birthdate = models.DateTimeField(db_column='BirthDate')
    hiredate = models.DateTimeField(db_column='HireDate')
    address = models.CharField(db_column='Address', max_length=60)
    city = models.CharField(db_column='City', max_length=15)
    region = models.CharField(db_column='Region', max_length=15)
    postalcode = models.CharField(db_column='PostalCode', max_length=10)
    country = models.CharField(db_column='Country', max_length=15)
    homephone = models.CharField(db_column='HomePhone', max_length=24)
    extension = models.CharField(db_column='Extension', max_length=4)
    photo = models.CharField(db_column='Photo', max_length=50)
    notes = models.TextField(db_column='Notes', blank=True, null=True)
    reportsto = models.ForeignKey('self', models.DO_NOTHING, db_column='ReportsTo', blank=True, null=True)

    class Meta:
        db_table = 'employees'


class Order(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustomerID')
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmployeeID')
    orderdate = models.DateTimeField(db_column='OrderDate')
    requireddate = models.DateTimeField(db_column='RequiredDate', blank=True, null=True)
    shippeddate = models.DateTimeField(db_column='ShippedDate', blank=True, null=True)
    # shipvia = models.ForeignKey('Shippers', models.DO_NOTHING, db_column='ShipVia')
    freight = models.FloatField(db_column='Freight')
    shipname = models.CharField(db_column='ShipName', max_length=40)
    shipaddress = models.CharField(db_column='ShipAddress', max_length=60)
    shipcity = models.CharField(db_column='ShipCity', max_length=15)
    shipregion = models.CharField(db_column='ShipRegion', max_length=15)
    shippostalcode = models.CharField(db_column='ShipPostalCode', max_length=10)
    shipcountry = models.CharField(db_column='ShipCountry', max_length=15)

    class Meta:
        db_table = 'orders'
