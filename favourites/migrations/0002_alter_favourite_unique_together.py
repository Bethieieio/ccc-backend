# Generated by Django 3.2.20 on 2023-08-03 19:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favourite',
            unique_together={('owner', 'recipe')},
        ),
    ]
