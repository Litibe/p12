# Generated by Django 4.0.3 on 2022-03-28 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=25, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('mobile', models.CharField(max_length=20, verbose_name='Mobile Number')),
                ('company_name', models.CharField(max_length=250, verbose_name='Compagny Name')),
                ('date_created', models.DateTimeField(verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(verbose_name='Date Updated')),
                ('sales_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]