# Generated by Django 4.1 on 2023-12-27 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("researchhub_case", "0021_authorclaimcase_target_doi"),
    ]

    operations = [
        migrations.RenameField(
            model_name="authorclaimcase",
            old_name="target_doi",
            new_name="target_paper_doi",
        ),
    ]