from django.db import models


class Categories(models.Model):
    categoryid = models.AutoField(db_column='CategoryID', primary_key=True)
    categoryname = models.CharField(db_column='CategoryName', unique=True, max_length=15)
    description = models.TextField(db_column='Description')
    picture = models.CharField(db_column='Picture', max_length=50)

    class Meta:
        db_table = 'categories'


class Suppliers(models.Model):
    supplierid = models.AutoField(db_column='SupplierID', primary_key=True)
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
    homepage = models.CharField(db_column='HomePage', max_length=255)

    class Meta:
        db_table = 'suppliers'


class Products(models.Model):
    productid = models.AutoField(db_column='ProductID', primary_key=True)
    productname = models.CharField(db_column='ProductName', max_length=40)
    supplierid = models.ForeignKey(Suppliers, models.DO_NOTHING, db_column='SupplierID')
    categoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='CategoryID')
    quantityperunit = models.CharField(db_column='QuantityPerUnit', max_length=20)
    unitprice = models.FloatField(db_column='UnitPrice')
    unitsinstock = models.PositiveSmallIntegerField(db_column='UnitsInStock')
    unitsonorder = models.PositiveSmallIntegerField(db_column='UnitsOnOrder')
    reorderlevel = models.PositiveSmallIntegerField(db_column='ReorderLevel')
    discontinued = models.CharField(db_column='Discontinued', max_length=1)

    class Meta:
        db_table = 'products'
