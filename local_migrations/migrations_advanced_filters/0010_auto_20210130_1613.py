# Generated by Django 3.0.6 on 2021-01-30 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advanced_filters', '0009_auto_20190912_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancedfilter',
            name='delete',
            field=models.BooleanField(null=False, default=False),
        ),
        migrations.AddField(
            model_name='advancedfilter',
            name='b64_fake_query',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='advancedfilter',
            name='b64_query',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
