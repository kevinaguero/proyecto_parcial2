# Generated by Django 4.1.3 on 2022-11-07 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vianda', '0005_alter_infosolicitudvianda_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infosolicitudvianda',
            name='nombre',
        ),
    ]
