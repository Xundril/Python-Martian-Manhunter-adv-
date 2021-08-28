# Generated by Django 3.2.6 on 2021-08-06 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Місто',
                'verbose_name_plural': 'Міста',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Країна',
                'verbose_name_plural': 'Країни',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Страва',
                'verbose_name_plural': 'Страви',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('position', models.CharField(blank=True, choices=[('manager', 'Manager'), ('waiter', 'Waiter'), ('cleaner', 'Cleaner'), ('cook', 'Cook')], max_length=16)),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонал',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(blank=True, choices=[('spring', 'Spring Menu'), ('summer', 'Summer Menu'), ('autumn', 'Autumn Menu'), ('winter', 'Winter Menu')], default='spring', max_length=20)),
                ('name', models.CharField(max_length=80)),
                ('dish', models.ManyToManyField(to='restaurants.Dish')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurants.city')),
                ('country', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurants.country')),
                ('menu', models.ManyToManyField(to='restaurants.Menu')),
                ('personal', models.ManyToManyField(to='restaurants.Employee')),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Ресторани',
            },
        ),
    ]