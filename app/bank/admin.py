from django.contrib import admin
from .models import Branch
from .models import Customer
from .models import Account
from .models import Product
# Register your models here.

admin.site.register(Branch)
admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Product)