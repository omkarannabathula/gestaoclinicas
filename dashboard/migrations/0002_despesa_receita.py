# Generated by Django 2.2.9 on 2020-01-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('receita_total', models.TextField(blank=True, null=True)),
                ('receita_total_anual', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('receita_total', models.TextField(blank=True, null=True)),
                ('receita_total_anual', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
