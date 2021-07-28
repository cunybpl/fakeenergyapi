from django.db.models import query
from django.shortcuts import render

from rest_framework import generics, permissions
from . import serializers, models

# Create your views here.

class FacilityListView(generics.ListAPIView):
    """ List of facilities in the dataset. 
    """ 
    queryset = models.Facility.objects.all().order_by('facility_id')
    serializer_class = serializers.FacilitySerializer
    filterset_fields = ['agency', 'building_type',]
    permission_classes = [permissions.IsAuthenticated]


class FacilityDetailView(generics.RetrieveAPIView): 
    """Retrieve a single facility by id
    """
    serializer_class = serializers.FacilitySerializer
    permission_classes = [permissions.IsAuthenticated]


class ConsumptionListView(generics.ListAPIView):
    """List of monthly usage data for each facility.
    """
    queryset = models.Consumption.objects.all().order_by('id')
    serializer_class = serializers.ConsumptionSerializer
    filterset_fields = ['facility', 'account', 'meter', 'year', 'month']
    permission_classes = [permissions.IsAuthenticated]


class CoefficientRecordView(generics.ListAPIView): 
    """List of coefficients for unit conversion to kbtu and co2 emissions.
    """

    queryset = models.CoefficientRecord.objects.all().order_by('id')
    serializer_class = serializers.CoefficientRecordSerializer 
    permission_classes = [permissions.IsAuthenticated]