# Generated by Django 5.0.3 on 2024-05-22 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='autor',
            field=models.CharField(max_length=50),
        ),
    ]