# Generated by Django 3.2.9 on 2021-11-22 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='like',
            new_name='likes',
        ),
    ]