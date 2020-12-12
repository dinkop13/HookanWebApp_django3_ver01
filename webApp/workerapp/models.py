from django.db import models

# Create your models here
class Items(models.Model):
    tittle = models.CharField(max_length=64)

    def __str__(self):
        return self.tittle

class Shops(models.Model):
    tittle = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

    def __str__(self):
        return self.tittle

class Storage(models.Model):
    id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    count = models.IntegerField()


    def __str__(self):
        name = "инв. №: {} - {}({} шт.)".format(self.id, self.item.__str__(), self.count)
        return name
