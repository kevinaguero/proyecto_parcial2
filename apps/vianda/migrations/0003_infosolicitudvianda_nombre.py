# Generated by Django 4.1.3 on 2022-11-07 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vianda', '0002_remove_infosolicitudvianda_itemsincluir_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='infosolicitudvianda',
            name='nombre',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
