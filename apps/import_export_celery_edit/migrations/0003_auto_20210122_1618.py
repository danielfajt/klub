# Generated by Django 2.2.17 on 2021-01-22 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('import_export_celery_edit', '0002_auto_20200624_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exportconnector',
            name='administrative_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aklub.AdministrativeUnit'),
        ),
    ]