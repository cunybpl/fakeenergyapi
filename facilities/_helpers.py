import pathlib 
from .serializers import FacilitySerializer, ConsumptionSerializer
import json
import csv
from rest_framework import serializers 
from typing import List

def read_facilities(p: pathlib.Path) -> List[FacilitySerializer]: 
    with open(p, 'r') as f: 
        data = json.load(f)
    return [FacilitySerializer(data=d) for d in data]

def read_consumption(p: pathlib.Path) -> List[ConsumptionSerializer]: 
    with open(p, 'r') as f: 
        reader = csv.DictReader(f)
        out = []
        for row in reader: 
            row['facility'] = row.pop('facility_id')
            out.append(ConsumptionSerializer(data=row))
        return out


def load_records(sers: List[serializers.ModelSerializer]) -> None: 
    for s in sers:
        s.is_valid(raise_exception=True)
        s.save()
