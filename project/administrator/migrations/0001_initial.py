# Generated by Django 5.0.3 on 2024-03-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id_administrator', models.AutoField(primary_key=True, serialize=False, verbose_name='id_administrator')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=300)),
                ('birth_date', models.DateField()),
                ('active', models.BooleanField()),
            ],
            options={
                'db_table': 'administrator',
            },
        ),
    ]