# Generated by Django 2.2.18 on 2021-02-12 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0094_auto_20210211_1311'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_auto_20210211_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='additional_photo_1',
            field=models.FileField(blank=True, null=True, upload_to='event_photos', verbose_name='Additional photo number 1'),
        ),
        migrations.AddField(
            model_name='event',
            name='additional_photo_2',
            field=models.FileField(blank=True, null=True, upload_to='event_photos', verbose_name='Additional photo number 2'),
        ),
        migrations.AddField(
            model_name='event',
            name='additional_photo_3',
            field=models.FileField(blank=True, null=True, upload_to='event_photos', verbose_name='Additional photo number 3'),
        ),
        migrations.AddField(
            model_name='event',
            name='additional_photo_4',
            field=models.FileField(blank=True, null=True, upload_to='event_photos', verbose_name='Additional photo number 4'),
        ),
        migrations.AddField(
            model_name='event',
            name='additional_photo_5',
            field=models.FileField(blank=True, null=True, upload_to='event_photos', verbose_name='Additional photo number 5'),
        ),
        migrations.AddField(
            model_name='event',
            name='additional_photo_6',
            field=models.FileField(blank=True, null=True, upload_to='event_photos', verbose_name='Additional photo number 6'),
        ),
        migrations.AddField(
            model_name='event',
            name='additional_question_1',
            field=models.CharField(blank=True, max_length=300, verbose_name='Additional question number 1'),
        ),
        migrations.AddField(
            model_name='event',
            name='additional_question_2',
            field=models.CharField(blank=True, max_length=300, verbose_name='Additional question number 2'),
        ),
        migrations.AddField(
            model_name='event',
            name='additional_question_3',
            field=models.CharField(blank=True, max_length=300, verbose_name='Additional question number 3'),
        ),
        migrations.AddField(
            model_name='event',
            name='invitation_text_1',
            field=models.TextField(blank=True, help_text='What to except, basic informations.', max_length=3000, verbose_name='Invitation: What to expect'),
        ),
        migrations.AddField(
            model_name='event',
            name='invitation_text_2',
            field=models.TextField(blank=True, help_text='Program of action.', max_length=3000, verbose_name='Invitation: What, where and how'),
        ),
        migrations.AddField(
            model_name='event',
            name='invitation_text_3',
            field=models.TextField(blank=True, help_text='Volunter help', max_length=3000, verbose_name='Invitation: Volunter help'),
        ),
        migrations.AddField(
            model_name='event',
            name='invitation_text_4',
            field=models.TextField(blank=True, help_text='Little sneek peek', max_length=3000, verbose_name='Invitation: Little sneek peek'),
        ),
        migrations.AddField(
            model_name='event',
            name='main_photo',
            field=models.FileField(blank=True, null=True, upload_to='event_photos', verbose_name='Main photo'),
        ),
        migrations.AddField(
            model_name='event',
            name='number_of_actions',
            field=models.PositiveIntegerField(default=1, verbose_name='Number of actions in given time period'),
        ),
        migrations.AddField(
            model_name='event',
            name='registration_method',
            field=models.CharField(choices=[('standard', 'Standard'), ('other_electronic', 'Other electrinoc'), ('by_email', "By organizer's email"), ('not_required', 'Not required'), ('full', 'Full, not anymore')], default='standard', max_length=128, verbose_name='Registration method'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start date'),
        ),
        migrations.AddField(
            model_name='event',
            name='web_url',
            field=models.URLField(blank=True, null=True, verbose_name='Url address of register form'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='administrative_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aklub.AdministrativeUnit', verbose_name='administrative unit'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='events.EventType', verbose_name='Event type'),
        ),
        migrations.CreateModel(
            name='OrganizingAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('administrative_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aklub.AdministrativeUnit', verbose_name='administrative unit')),
            ],
            options={
                'verbose_name': 'Organizing association',
                'verbose_name_plural': 'Organizing associations',
            },
        ),
        migrations.CreateModel(
            name='OrganizationTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_be_contacted', models.BooleanField(default=False, verbose_name='Can be contacted')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event', verbose_name='Event')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.OrganizationPosition', verbose_name='Position')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('place', models.CharField(blank=True, max_length=100, verbose_name='Place')),
                ('region', models.CharField(blank=True, max_length=100, verbose_name='Region')),
                ('gps', models.CharField(blank=True, max_length=200, verbose_name='GPS location')),
                ('administrative_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aklub.AdministrativeUnit', verbose_name='administrative unit')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Location', verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='organization_team',
            field=models.ManyToManyField(through='events.OrganizationTeam', to=settings.AUTH_USER_MODEL, verbose_name='Organization team'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizing_associations',
            field=models.ManyToManyField(blank=True, to='events.OrganizingAssociation', verbose_name='Organizing associations'),
        ),
    ]
