# Generated by Django 5.1.6 on 2025-02-21 07:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('station', models.CharField(max_length=255)),
                ('notification', models.IntegerField(unique=True)),
                ('date', models.DateField()),
                ('client_name', models.CharField(max_length=255)),
                ('place_of_transfer', models.CharField(max_length=255)),
                ('locomotive', models.CharField(max_length=255)),
                ('route_belonging', models.CharField(max_length=255)),
                ('client_representative', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'documents',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wagon', models.IntegerField()),
                ('container_and_size', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('control_mark', models.CharField(max_length=255)),
                ('operation', models.CharField(max_length=255)),
                ('cargo_names', models.TextField()),
                ('note', models.TextField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gu_2b.document')),
            ],
            options={
                'db_table': 'cargo',
            },
        ),
    ]
