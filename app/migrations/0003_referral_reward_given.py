# Generated by Django 5.0.4 on 2024-12-27 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_investmentplan_site_transferedlg_wallet_withdrwal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='reward_given',
            field=models.BooleanField(default=False),
        ),
    ]
