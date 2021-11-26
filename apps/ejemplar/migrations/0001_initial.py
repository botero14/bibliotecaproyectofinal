# Generated by Django 3.2.9 on 2021-11-25 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('localizacion', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'autor',
                'verbose_name_plural': 'autores',
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('localizacion', models.CharField(max_length=30)),
                ('ejemplar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejemplar.ejemplar', verbose_name='libros')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.libro', verbose_name='libros')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario', verbose_name='autores')),
            ],
        ),
    ]