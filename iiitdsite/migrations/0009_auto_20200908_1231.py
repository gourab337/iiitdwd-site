# Generated by Django 3.0.8 on 2020-09-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiitdsite', '0008_auto_20200908_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultypageinfo',
            name='phd_info',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='facultypageinfo',
            name='phd_info_hindi',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='facultypageinfo',
            name='phd_info_kannada',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
