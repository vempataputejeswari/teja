from django.contrib import admin


# Register your models here.
from mysales.models import product

admin.site.register(product)
class productAdmin(admin.ModelAdmin):
	exclude = ('volume')  