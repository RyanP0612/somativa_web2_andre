# Generated by Django 5.0.3 on 2024-05-30 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='devolucaoPrevista',
            field=models.DateField(blank=True, null=True),
        ),
    ]
