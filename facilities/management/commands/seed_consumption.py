import pathlib 
from django.conf import settings
from django.core.management.base import BaseCommand 
from django.db import transaction

import logging 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

consumption_path = pathlib.Path(settings.DEFAULT_FIXTURES_DIR) / 'anon-consumption.csv'


from facilities._helpers import read_consumption, load_records

class Command(BaseCommand): 
    """Seeds the database with file fixtures generated from scripts in pytrainer. 
    First loads facilities, then consumption tables
    """ 

    def handle(self, *args, **options): 
        with transaction.atomic():
            logger.info('Loading consumption data')
            consump = read_consumption(consumption_path)
            load_records(consump)