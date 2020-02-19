from django.db import models


class Category(models.Model):
    categoryid = models.AutoField(db_column='CategoryID', primary_key=True)
    category_name = models.CharField(db_column='CategoryName', unique=True, max_length=15)
    description = models.TextField(db_column='Description')
    picture = models.CharField(db_column='Picture', max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'categories'


class Supplier(models.Model):
    supplierid = models.AutoField(db_column='SupplierID', primary_key=True)
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
    homepage = models.CharField(db_column='HomePage', max_length=255)

    class Meta:
        db_table = 'suppliers'


class Product(models.Model):
    productid = models.AutoField(db_column='ProductID', primary_key=True)
    product_name = models.CharField(db_column='ProductName', max_length=40)
    supplier = models.ForeignKey(Supplier, models.DO_NOTHING, db_column='SupplierID')
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='CategoryID')
    quantityperunit = models.CharField(db_column='QuantityPerUnit', max_length=20)
    unit_price = models.FloatField(db_column='UnitPrice')
    unitsinstock = models.PositiveSmallIntegerField(db_column='UnitsInStock')
    unitsonorder = models.PositiveSmallIntegerField(db_column='UnitsOnOrder')
    reorderlevel = models.PositiveSmallIntegerField(db_column='ReorderLevel')
    discontinued = models.CharField(db_column='Discontinued', max_length=1)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'products'
