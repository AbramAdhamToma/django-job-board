# Generated by Django 4.0.1 on 2022-01-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_alter_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Internship', 'Internship'), ('Work From Home', 'Work From Home'), ('Shift Based', 'Shift Based')], max_length=15),
        ),
    ]
