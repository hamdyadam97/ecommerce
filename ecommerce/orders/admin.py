from django.contrib import admin
from .models import Order
# Register your models here.

class OrederAdmin(admin.ModelAdmin):

    class Meta:
        model = Order



admin.site.register(Order,OrederAdmin)
