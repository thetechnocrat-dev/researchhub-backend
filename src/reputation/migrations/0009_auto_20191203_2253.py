# Generated by Django 2.2.8 on 2019-12-03 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0008_auto_20191203_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawal',
            name='amount_decimal_part',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='amount_integer_part',
            field=models.BigIntegerField(default=0),
        ),
    ]