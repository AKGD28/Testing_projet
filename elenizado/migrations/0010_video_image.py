# Generated by Django 2.2.12 on 2020-06-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elenizado', '0009_auto_20200629_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(default='video/video.png', upload_to='video/image'),
        ),
    ]