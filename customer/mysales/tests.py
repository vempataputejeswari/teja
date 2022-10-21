from django.test import TestCase
from mysales.models import product

# Create your tests here.

class ProductTestCase(TestCase):
	def unit_test_record(self):
		obj = product (name = "tejeswari",
			description= "my name is teju",
	        costitem= 280,
	        stockquantity= 4,)
	    obj.save()
	    self.assertEquals(obj.StockQuantity, 4, "Quantity Mismatch")
	    self.assertEquals(obj.CostItem, 280, "product Cost Mismatch")
	    self.assertEquals(obj.volume, 1120.00, "volume Mismatch")


