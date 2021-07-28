from django.contrib import admin

# Register your models here.
from .models import CoefficientRecord 

@admin.register(CoefficientRecord)
class CoefficientRecordAdmin(admin.ModelAdmin): 
    pass