# Generated by Django 3.1.7 on 2021-03-31 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=200)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
                ('publishedDateTime', models.DateTimeField()),
                ('thumbnailUrls', models.URLField()),
                ('chanel_id', models.CharField(max_length=500)),
                ('chanel_title', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
