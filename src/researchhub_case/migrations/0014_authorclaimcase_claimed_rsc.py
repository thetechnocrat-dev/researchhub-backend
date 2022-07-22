# Generated by Django 2.2 on 2022-04-06 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0049_auto_20220406_0020'),
        ('researchhub_case', '0013_auto_20220217_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorclaimcase',
            name='claimed_rsc',
            field=models.ManyToManyField(blank=True, null=True, related_name='claim_case', to='reputation.authorrsc'),
        ),
    ]
