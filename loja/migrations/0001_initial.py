# Generated by Django 3.1.3 on 2020-11-12 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=100)),
                ('logo', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'loja',
            },
        ),
    ]