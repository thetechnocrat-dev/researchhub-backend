# Generated by Django 2.2 on 2021-07-01 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0080_merge_20210611_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='authors',
            field=models.ManyToManyField(blank=True, help_text='Author that participated in the research paper', related_name='authored_papers', to='user.Author'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, help_text='RH User account that submitted this paper. NOTE: user didnt necessarily had to be the author', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='papers', to=settings.AUTH_USER_MODEL),
        ),
    ]
