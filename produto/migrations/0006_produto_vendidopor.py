# Generated by Django 3.1.3 on 2020-11-12 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_auto_20201112_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='vendidoPor',
            field=models.SlugField(default='candyStore', max_length=100),
        ),
    ]
