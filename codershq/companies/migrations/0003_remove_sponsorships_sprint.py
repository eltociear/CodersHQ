# Generated by Django 3.2.11 on 2022-01-26 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20220119_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsorships',
            name='sprint',
        ),
    ]
