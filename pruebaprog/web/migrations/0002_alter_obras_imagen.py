# Generated by Django 4.2.2 on 2023-07-08 22:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obras',
            name='imagen',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='obras'),
            preserve_default=False,
        ),
    ]
