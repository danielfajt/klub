# Generated by Django 2.2.18 on 2021-02-11 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='eventtype',
            options={'verbose_name': 'Event type', 'verbose_name_plural': 'Event types'},
        ),
    ]
