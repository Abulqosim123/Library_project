# Generated by Django 4.2.7 on 2023-11-13 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='subtile',
            new_name='subtitle',
        ),
    ]
