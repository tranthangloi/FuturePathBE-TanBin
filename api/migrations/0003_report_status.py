# Generated by Django 5.2 on 2025-04-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_adminsystem_account_alter_adminsystem_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
