# Generated by Django 4.1 on 2022-09-12 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('show', '0021_remove_nomelista_celular_remove_nomelista_cpf_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='nomelista',
            unique_together={('roqueiro', 'lista_reserva')},
        ),
    ]
