# Generated by Django 3.1.3 on 2020-11-12 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_auto_20201112_0433'),
        ('produto', '0009_auto_20201112_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='loja',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.PROTECT, to='loja.loja'),
        ),
    ]