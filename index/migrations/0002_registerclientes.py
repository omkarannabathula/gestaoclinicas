# Generated by Django 2.2.5 on 2019-10-07 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerclientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=30, null=True)),
                ('sobrenome', models.CharField(blank=True, max_length=30, null=True)),
                ('cnpj', models.CharField(max_length=11, null=True)),
                ('celular', models.CharField(blank=True, max_length=9, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
