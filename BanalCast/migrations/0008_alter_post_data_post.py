# Generated by Django 3.2.4 on 2021-06-27 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BanalCast', '0007_alter_post_data_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]