# Generated by Django 2.2.24 on 2021-12-12 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_event_datetime_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime_from',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date from'),
        ),
    ]