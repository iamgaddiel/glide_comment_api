# Generated by Django 3.2.9 on 2021-11-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_blog_like_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='liker',
            field=models.CharField(max_length=32),
        ),
    ]