# Generated by Django 2.2.9 on 2020-01-09 08:31
import django.core.validators
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0061_auto_20200114_1130'),
    ]

    def default_values_money_acccount(apps, schema_editor):
        db_alias = schema_editor.connection.alias
        MoneyAccount = apps.get_model("aklub", "MoneyAccount")
        AdministrativeUnit = apps.get_model("aklub", "AdministrativeUnit")
        for obj in MoneyAccount.objects.using(db_alias).all():
            if not hasattr(obj, 'administrative_unit'):
                unit, _ = AdministrativeUnit.objects.using(db_alias).get_or_create(name='change_this_unit_then_delete')
                obj.administrative_unit = unit
                obj.save()

    def default_values_preference(apps, schema_editor):
        db_alias = schema_editor.connection.alias
        Preference = apps.get_model("aklub", "Preference")
        AdministrativeUnit = apps.get_model("aklub", "AdministrativeUnit")
        for obj in Preference.objects.using(db_alias).all():
            if not hasattr(obj, 'administrative_unit'):
                unit, _ = AdministrativeUnit.objects.using(db_alias).get_or_create(name='change_this_unit_then_delete')
                obj.administrative_unit = unit
                obj.save()

    def default_values_taxconfirmation(apps, schema_editor):
        db_alias = schema_editor.connection.alias
        TaxConfirmation = apps.get_model("aklub", "TaxConfirmation")
        AdministrativeUnit = apps.get_model("aklub", "AdministrativeUnit")

        for obj in TaxConfirmation.objects.using(db_alias).all():
            if not hasattr(obj, 'administrative_unit'):
                unit, _ = AdministrativeUnit.objects.using(db_alias).get_or_create(name='change_this_unit_then_delete')
                obj.administrative_unit = unit
                obj.save()



    operations = [
        migrations.RunPython(default_values_money_acccount, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(default_values_preference, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(default_values_taxconfirmation, reverse_code=migrations.RunPython.noop),

        migrations.AlterField(
            model_name='moneyaccount',
            name='administrative_unit',
            field=models.ForeignKey(null=False, blank=False, on_delete=django.db.models.deletion.CASCADE, to='aklub.AdministrativeUnit', verbose_name='administrative unit'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='administrative_unit',
            field=models.ForeignKey(null=False, blank=False, on_delete=django.db.models.deletion.CASCADE, to='aklub.AdministrativeUnit', verbose_name='administrative unit'),
        ),
        migrations.AlterField(
            model_name='taxconfirmation',
            name='administrative_unit',
            field=models.ForeignKey(null=False, blank=False, on_delete=django.db.models.deletion.CASCADE, to='aklub.AdministrativeUnit', verbose_name='administrative unit'),
        ),

    ]
