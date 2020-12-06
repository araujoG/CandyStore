# Generated by Django 3.1.3 on 2020-11-21 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0004_auto_20201112_0519'),
        ('produto', '0013_auto_20201121_0343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='categoria.categoria'),
        ),
    ]
