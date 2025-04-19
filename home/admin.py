from django.contrib import admin
from .models import MaqomlarModel,MaqomlarTuri

# Register your models here.

admin.site.register(MaqomlarModel)
admin.site.register(MaqomlarTuri)