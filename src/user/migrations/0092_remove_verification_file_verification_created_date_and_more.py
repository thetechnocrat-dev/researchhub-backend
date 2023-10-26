# Generated by Django 4.1 on 2023-10-05 22:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0091_action_is_removed"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="verification",
            name="file",
        ),
        migrations.AddField(
            model_name="verification",
            name="created_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="verification",
            name="details",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="verification",
            name="related_author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="verification",
                to="user.author",
            ),
        ),
        migrations.AddField(
            model_name="verification",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("APPROVED", "APPROVED"),
                    ("DENIED", "DENIED"),
                    ("INITIATED", "INITIATED"),
                ],
                default="INITIATED",
                max_length=16,
            ),
        ),
        migrations.AddField(
            model_name="verification",
            name="updated_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name="VerificationFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("file", models.FileField(upload_to="uploads/verification/%Y/%m/%d")),
                (
                    "verification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="user.verification",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]