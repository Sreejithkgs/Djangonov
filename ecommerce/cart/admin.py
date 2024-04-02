from django.contrib import admin
from django.http import HttpResponse
from .models import cart,order,account
admin.site.register(cart)
admin.site.register(order)
admin.site.register(account)

# Register your models here.
