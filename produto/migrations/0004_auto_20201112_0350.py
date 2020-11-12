# Generated by Django 3.1.3 on 2020-11-12 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_produto_secao'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='avaliacao',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='produto',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]
