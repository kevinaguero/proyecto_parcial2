# Generated by Django 4.1.3 on 2022-11-07 21:48

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
            name='ItemVianda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=20)),
                ('esta_activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='InfoSolicitudVianda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoMenu', models.IntegerField(choices=[(1, 'Normal'), (2, 'Vegetariano'), (3, 'Diabetico')])),
                ('frecuencia', models.IntegerField(choices=[(1, 'semanal'), (2, 'quincenal')])),
                ('fechaInicioVianda', models.DateField()),
                ('cantidadViandas', models.IntegerField()),
                ('estadoVianda', models.IntegerField(choices=[(1, 'Pendiente'), (2, 'Confirmado'), (3, 'Cancelado')])),
                ('itemsincluir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vianda.itemvianda')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
