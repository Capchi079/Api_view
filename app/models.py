from django.db import models

# Create your models here.


class Product_Catagory(models.Model):
    Pcid=models.IntegerField()
    Pcname=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.Pcname

class Product(models.Model):
    Pcname=models.ForeignKey(Product_Catagory, on_delete=models.CASCADE)
    Pid=models.IntegerField(primary_key=True)
    Pname=models.CharField(max_length=100)
    Pprice=models.IntegerField()
    Pdescription=models.CharField(max_length=200)
    Pdate=models.DateField(default='8/6/23')
    def __str__(self):
        return self.Pname
