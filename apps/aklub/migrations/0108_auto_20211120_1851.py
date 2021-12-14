# Generated by Django 3.1 on 2021-11-20 17:51

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0107_payment_custom_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='custom_fields',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='taxconfirmationfield',
            name='field',
            field=models.CharField(choices=[], max_length=36, verbose_name='field'),
        ),
    ]
