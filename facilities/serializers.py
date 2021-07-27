from rest_framework import serializers 
from . import models 


class FacilitySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = models.Facility
        fields = '__all__'


class ConsumptionSerializer(serializers.ModelSerializer): 
    
    class Meta: 
        model = models.Consumption
        fields = [
            'facility', 
            'account', 
            'meter', 
            'epa_energy_type', 
            'allocated_consumption', 
            'consumption_unit', 
            'reading_type', 
            'year', 
            'month'
        ]