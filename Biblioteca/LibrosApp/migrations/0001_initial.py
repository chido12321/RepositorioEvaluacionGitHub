# Generated by Django 4.2.2 on 2023-07-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('autor', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=10)),
            ],
        ),
    ]