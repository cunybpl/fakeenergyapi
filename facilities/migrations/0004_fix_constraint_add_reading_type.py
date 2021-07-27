# Generated by Django 3.2.5 on 2021-07-27 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0003_fix_constraint'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='consumption',
            name='consumption__constraint',
        ),
        migrations.AddConstraint(
            model_name='consumption',
            constraint=models.UniqueConstraint(fields=('facility', 'account', 'meter', 'year', 'month', 'reading_type'), name='consumption__constraint'),
        ),
    ]