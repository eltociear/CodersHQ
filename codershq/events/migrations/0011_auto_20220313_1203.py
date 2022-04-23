# Generated by Django 3.2.11 on 2022-03-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20220313_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventbrite_id',
            field=models.CharField(default='', max_length=11, verbose_name='eventbrite id'),
        ),
        migrations.AlterField(
            model_name='event',
            name='capacity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of seats available (if not online)'),
        ),
    ]
