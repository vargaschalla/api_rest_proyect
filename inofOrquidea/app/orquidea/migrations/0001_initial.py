# Generated by Django 3.2.8 on 2021-10-21 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orquidea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_crecimiento', models.CharField(max_length=30)),
                ('nombre_comun', models.CharField(max_length=30, unique=True)),
                ('floracion', models.CharField(max_length=30)),
                ('duracion_flor', models.CharField(max_length=30)),
                ('tamaño_flor', models.CharField(max_length=30)),
                ('ubicacion', models.CharField(max_length=60)),
            ],
        ),
    ]
