# Generated by Django 3.1.7 on 2021-03-31 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210331_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videos',
            old_name='thumbnailUrls',
            new_name='thumbnailsUrls',
        ),
        migrations.AlterField(
            model_name='videos',
            name='channel_title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
