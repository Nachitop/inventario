# Generated by Django 3.0 on 2019-12-15 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipos', '0001_initial'),
        ('facultades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('numero_cuenta', models.CharField(max_length=9)),
                ('status', models.SmallIntegerField(choices=[(3, 'Prestado')], default=(3, 'Prestado'))),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.Equipo')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facultades.Ubicacion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
