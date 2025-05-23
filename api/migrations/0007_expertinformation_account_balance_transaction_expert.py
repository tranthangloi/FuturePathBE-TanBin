# Generated by Django 5.2 on 2025-05-02 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_expertinformation_certifications_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertinformation',
            name='account_balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AddField(
            model_name='transaction',
            name='expert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.expertinformation'),
        ),
    ]
