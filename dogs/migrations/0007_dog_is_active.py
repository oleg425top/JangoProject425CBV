# Generated by Django 5.0.13 on 2025-04-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0006_dogparent'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активность'),
        ),
    ]
