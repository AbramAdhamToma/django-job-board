# Generated by Django 4.0.1 on 2022-01-31 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_alter_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
