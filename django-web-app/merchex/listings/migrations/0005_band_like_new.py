# Generated by Django 4.0.3 on 2022-03-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]
