# Generated by Django 5.0.4 on 2025-02-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_deposite_walletpaidon'),
    ]

    operations = [
        migrations.AddField(
            model_name='oninvestment',
            name='coininvestment',
            field=models.CharField(blank=True, default=None, max_length=4000),
        ),
    ]
