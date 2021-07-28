from django.db import models


class Facility(models.Model): 

    facility_id = models.IntegerField(primary_key=True)
    lat = models.FloatField()
    lon = models.FloatField()
    sqft = models.IntegerField(null=True)
    agency = models.CharField(max_length=50)
    building_type = models.CharField(max_length=50)

    class Meta: 
        indexes = [
            models.Index(fields=['agency']),
            models.Index(fields=['building_type']), 
            models.Index(fields=['agency', 'building_type'])
        ]


class Consumption(models.Model): 

    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    account = models.CharField(max_length=50)
    meter = models.CharField(max_length=50)
    epa_energy_type = models.CharField(max_length=50)
    allocated_consumption = models.FloatField()
    consumption_unit = models.CharField(max_length=15)
    reading_type = models.CharField(max_length=5, blank=True, null=True)
    year = models.IntegerField()
    month = models.IntegerField()

    class Meta: 
        indexes = [
            models.Index(fields=['facility']), 
            models.Index(fields=['facility', 'meter']),
            models.Index(fields=['facility', 'year']),
            models.Index(fields=['facility', 'month']), 
            models.Index(fields=['facility', 'epa_energy_type'])
        ]

class CoefficientRecord(models.Model): 
    
    epa_energy_type =  models.CharField(max_length=50, unique=True)
    site_to_source_ratio = models.FloatField()
    kbtu_coeff = models.FloatField()
    co2e_coeff = models.FloatField()    

    class Meta:
        indexes = [
            models.Index(fields=['epa_energy_type'])
        ]
