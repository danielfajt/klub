# Generated by Django 2.2.18 on 2021-02-11 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0011_auto_20201112_1444'),
        ('events', "0001_initial")
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Event', verbose_name='Event'),
        ),
        migrations.AlterField(
            model_name='petitionsignature',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Event', verbose_name='Event'),
        ),
    ]