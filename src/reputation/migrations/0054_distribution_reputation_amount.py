# Generated by Django 2.2 on 2022-05-25 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0053_distribution_giver'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribution',
            name='reputation_amount',
            field=models.IntegerField(default=0),
        ),
    ]
