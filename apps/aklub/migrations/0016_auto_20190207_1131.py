# Generated by Django 2.1.5 on 2019-02-07 10:31

import aklub.autocom
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0015_auto_20190206_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masscommunication',
            name='template',
            field=models.TextField(help_text='Template can contain following variable substitutions: <br/>{mr|mrs} or {mr/mrs}, $addressment, $name, $firstname, $surname, $street, $city, $zipcode, $email, $telephone, $regular_amount, $regular_frequency, $var_symbol, $last_payment_amount, $auth_token', max_length=50000, null=True, validators=[aklub.autocom.gendrify_text, django.core.validators.RegexValidator('^([^$]*(\\$(addressment|name|firstname|surname|street|city|zipcode|email|telephone|regular_amount|regular_frequency|var_symbol|last_payment_amount|auth_token)\\b)?)*$', 'Unknown variable')], verbose_name='Template'),
        ),
    ]
