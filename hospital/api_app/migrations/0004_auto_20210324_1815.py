# Generated by Django 3.1.7 on 2021-03-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_bedavailability_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedavailability',
            name='patient_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]