# Generated by Django 2.2 on 2021-09-02 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hypothesis', '0004_auto_20210812_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='hypothesis',
            name='discussion_count',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]