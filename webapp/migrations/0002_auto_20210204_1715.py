# Generated by Django 3.1.6 on 2021-02-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switchboard',
            name='IP_of_switchboard',
            field=models.CharField(max_length=100),
        ),
    ]