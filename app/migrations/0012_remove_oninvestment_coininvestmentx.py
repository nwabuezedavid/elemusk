# Generated by Django 5.0.4 on 2025-02-05 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_oninvestment_coininvestmentx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oninvestment',
            name='coininvestmentx',
        ),
    ]
