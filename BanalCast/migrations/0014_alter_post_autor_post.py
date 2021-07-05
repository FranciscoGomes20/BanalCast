# Generated by Django 3.2.4 on 2021-07-04 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BanalCast', '0013_alter_post_texto_poste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]