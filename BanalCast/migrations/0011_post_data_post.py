# Generated by Django 3.2.4 on 2021-06-28 00:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BanalCast', '0010_remove_post_data_poste'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='data_post',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
