from django.contrib import admin
from gobetween_app.models import user_reg,driver_reg,comp_reg
# Register your models here.

admin.site.register(user_reg)
admin.site.register(driver_reg)
admin.site.register(comp_reg)