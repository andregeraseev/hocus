# Generated by Django 4.1 on 2022-08-31 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomelista', '0003_remove_nomelista_pessoa_nomelista_pessoa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nomelista',
            name='show',
        ),
    ]