# Generated by Django 4.2.2 on 2023-07-09 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_obras_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obras',
            name='imagen',
            field=models.ImageField(null=True, upload_to='obras'),
        ),
    ]
