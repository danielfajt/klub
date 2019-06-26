# Generated by Django 2.2.2 on 2019-06-26 13:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import stdnumfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0028_auto_20190621_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('ico', stdnumfield.models.StdNumField(alphabets=[None], blank=True, default=None, error_messages={'stdnum_format': 'IČO není zadáno ve správném formátu. Zkontrolujte že číslo má osm číslic a případně ho doplňte nulami zleva.'}, formats=['cz.dic'], null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'IČO musí být číslo')], verbose_name='IČO')),
            ],
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='bank_account_number',
            field=models.CharField(max_length=50, verbose_name='Bank account number'),
        ),
        migrations.AlterField(
            model_name='userbankaccount',
            name='bank_account_number',
            field=models.CharField(max_length=50, verbose_name='Bank account number'),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='administrative_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aklub.AdministrativeUnit', verbose_name='administrative unit'),
        ),
        migrations.AddField(
            model_name='event',
            name='administrative_units',
            field=models.ManyToManyField(blank=True, to='aklub.AdministrativeUnit', verbose_name='administrative units'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='administrated_units',
            field=models.ManyToManyField(blank=True, related_name='administrators', to='aklub.AdministrativeUnit', verbose_name='administrated units'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='administrative_units',
            field=models.ManyToManyField(blank=True, to='aklub.AdministrativeUnit', verbose_name='administrative units'),
        ),
    ]
