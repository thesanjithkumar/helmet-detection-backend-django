# Generated by Django 4.1.7 on 2023-03-30 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Images", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="images",
            name="name",
        ),
        migrations.AlterField(
            model_name="images",
            name="pub_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 3, 30, 7, 8, 1, 421348, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]