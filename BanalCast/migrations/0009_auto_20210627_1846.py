# Generated by Django 3.2.4 on 2021-06-27 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BanalCast', '0008_alter_post_data_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='data_post',
        ),
        migrations.AddField(
            model_name='post',
            name='data_poste',
            field=models.DateField(blank=True, null=True),
        ),
    ]
