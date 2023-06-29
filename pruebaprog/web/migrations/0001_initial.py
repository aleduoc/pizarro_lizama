# Generated by Django 4.2.2 on 2023-06-29 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[(0, 'Consulta'), (1, 'Sugerencia'), (2, 'Felicitaciones')])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Obras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='obras')),
            ],
        ),
    ]
