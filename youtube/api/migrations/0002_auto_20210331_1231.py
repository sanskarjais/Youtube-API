# Generated by Django 3.1.7 on 2021-03-31 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videos',
            old_name='chanel_id',
            new_name='channel_id',
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='chanel_title',
            new_name='channel_title',
        ),
    ]
