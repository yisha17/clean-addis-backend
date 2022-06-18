from django.contrib import admin

# Register your models here.
from .models import User,Address,Company,Waste

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Company)
admin.site.register(Waste)