# Generated by Django 5.0.4 on 2025-02-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_oninvestment_coininvestmentx'),
    ]

    operations = [
        migrations.AddField(
            model_name='oninvestment',
            name='coininvestmentx',
            field=models.CharField(default='None', max_length=4000),
        ),
    ]
