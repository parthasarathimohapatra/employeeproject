# Generated by Django 3.0.3 on 2020-05-25 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='star_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date',
            field=models.DateField(),
        ),
    ]