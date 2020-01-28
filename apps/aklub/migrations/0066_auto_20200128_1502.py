# Generated by Django 2.2.9 on 2020-01-28 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0065_automaticcommunication_administrative_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automaticcommunication',
            name='administrative_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aklub.AdministrativeUnit', verbose_name='administrative unit'),
        ),
        migrations.AlterField(
            model_name='masscommunication',
            name='administrative_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aklub.AdministrativeUnit', verbose_name='administrative unit'),
        ),
    ]
