# Generated by Django 3.1.3 on 2020-11-12 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='categoriaPai',
            field=models.CharField(db_index=True, default='', max_length=100),
        ),
    ]
