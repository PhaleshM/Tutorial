# Generated by Django 3.1.4 on 2020-12-21 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20201221_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='disciption',
            new_name='discription',
        ),
    ]
