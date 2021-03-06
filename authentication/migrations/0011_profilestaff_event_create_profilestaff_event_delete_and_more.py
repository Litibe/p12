# Generated by Django 4.0.3 on 2022-03-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_profilestaff_contract_create_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilestaff',
            name='event_create',
            field=models.BooleanField(default=False, verbose_name='Event - Create'),
        ),
        migrations.AddField(
            model_name='profilestaff',
            name='event_delete',
            field=models.BooleanField(default=False, verbose_name='Event - Delete'),
        ),
        migrations.AddField(
            model_name='profilestaff',
            name='event_read',
            field=models.BooleanField(default=False, verbose_name='Event - Read'),
        ),
        migrations.AddField(
            model_name='profilestaff',
            name='event_update',
            field=models.BooleanField(default=False, verbose_name='Event - Update'),
        ),
        migrations.AddField(
            model_name='profilestaff',
            name='need_create',
            field=models.BooleanField(default=False, verbose_name='Need - Create'),
        ),
        migrations.AddField(
            model_name='profilestaff',
            name='need_delete',
            field=models.BooleanField(default=False, verbose_name='Need - Delete'),
        ),
        migrations.AddField(
            model_name='profilestaff',
            name='need_read',
            field=models.BooleanField(default=False, verbose_name='Need - Read'),
        ),
        migrations.AddField(
            model_name='profilestaff',
            name='need_update',
            field=models.BooleanField(default=False, verbose_name='Need - Update'),
        ),
    ]
