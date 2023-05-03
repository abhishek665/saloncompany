from django.contrib import admin
from .models import Services, SubCategory, AtomCategory, Order
# Register your models here.

admin.site.register(Services)
admin.site.register(SubCategory)
admin.site.register(AtomCategory)
admin.site.register(Order)