# Generated by Django 3.2.4 on 2021-07-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BanalCast', '0017_rename_imgens_poste_post_imagens_poste'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link_app',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='link_apple',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='link_google',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='link_spotify',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
