# Generated by Django 3.1.3 on 2020-11-26 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0008_auto_20201125_2310'),
        ('produto', '0017_auto_20201122_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='categoria.categoria'),
        ),
    ]