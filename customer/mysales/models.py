from django.db import models
from django.db.models.signals import pre_save
# Create your models here.

class product (models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	costitem = models.DecimalField(max_digits=10,decimal_places=2)
	stockquantity = models.IntegerField()
	volume = models.IntegerField()
	def __str__ (self):
	    return self.name



def calcucate_volume(instance, sender, *args, **kwargs):
	instance.volume = float(instance.costitem * instance.stockquantity)

pre_save.connect(calcucate_volume, sender=product)