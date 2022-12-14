# Generated by Django 4.1 on 2022-08-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=300)),
                ('foto_banner', models.ImageField(blank=True, upload_to='static/banners')),
                ('publicada', models.BooleanField(default=False)),
            ],
        ),
    ]
