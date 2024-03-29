# Generated by Django 4.1.7 on 2023-02-18 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2023, 2, 18, 14, 4, 34, 768751, tzinfo=datetime.timezone.utc))),
                ('location', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='fine_images')),
            ],
        ),
    ]
