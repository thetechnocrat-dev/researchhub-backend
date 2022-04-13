# Generated by Django 2.2 on 2022-03-29 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0089_auto_20220308_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papersubmission',
            name='paper_status',
            field=models.CharField(choices=[('COMPLETE', 'COMPLETE'), ('INITIATED', 'INITIATED'), ('FAILED', 'FAILED'), ('FAILED', 'FAILED_DUPLICATE'), ('FAILED_TIMEOUT', 'FAILED_TIMEOUT'), ('PROCESSING', 'PROCESSING'), ('PROCESSING_CROSSREF', 'PROCESSING_CROSSREF'), ('PROCESSING_MANUBOT', 'PROCESSING_MANUBOT'), ('PROCESSING_DOI', 'PROCESSING_DOI')], default='INITIATED', max_length=32),
        ),
    ]