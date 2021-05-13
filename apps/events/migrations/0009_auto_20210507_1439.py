# Generated by Django 2.2.20 on 2021-05-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20210429_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='responsible_person',
            field=models.CharField(blank=True, max_length=128, verbose_name='Responsible person'),
        ),
        migrations.AlterField(
            model_name='event',
            name='diet',
            field=models.CharField(blank=True, choices=[('', '---'), ('vegetarian', 'Vegetarian'), ('non_vegetarian', 'Non-vegetarian'), ('can_choose', 'Can choose')], max_length=128, verbose_name='Diet'),
        ),
        migrations.AlterField(
            model_name='event',
            name='participation_fee',
            field=models.CharField(blank=True, max_length=128, default="", verbose_name='Participation fee'),
        ),
    ]
