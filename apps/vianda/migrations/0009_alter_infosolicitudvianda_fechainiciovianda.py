# Generated by Django 4.1.3 on 2022-11-07 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vianda', '0008_alter_infosolicitudvianda_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosolicitudvianda',
            name='fechaInicioVianda',
            field=models.DateTimeField(),
        ),
    ]
