# Generated by Django 4.1 on 2022-09-08 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0005_remove_show_lista_pix'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowNomelista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='show.nomelista', unique='show')),
                ('show', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='show.show')),
            ],
        ),
    ]
