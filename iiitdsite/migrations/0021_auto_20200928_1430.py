# Generated by Django 3.0.8 on 2020-09-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiitdsite', '0020_auto_20200918_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='image_link',
        ),
        migrations.AddField(
            model_name='events',
            name='image',
            field=models.ImageField(blank=True, upload_to='EventsCover/<django.db.models.fields.CharField>'),
        ),
    ]
