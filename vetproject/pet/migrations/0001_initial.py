# Generated by Django 3.2.8 on 2022-02-08 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('type', models.CharField(max_length=100, verbose_name='Type')),
                ('variety', models.CharField(max_length=100, verbose_name='Variety')),
                ('explain', models.CharField(max_length=100, verbose_name='Explain')),
                ('age', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Age')),
            ],
            options={
                'verbose_name': 'Pet',
                'verbose_name_plural': 'Pets',
            },
        ),
        migrations.CreateModel(
            name='PetOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=100, verbose_name='PetOwner Name')),
                ('pet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pet.pet', verbose_name='Pet Info')),
            ],
            options={
                'verbose_name': 'Pet Owner',
                'verbose_name_plural': 'Pet Owners',
            },
        ),
    ]
