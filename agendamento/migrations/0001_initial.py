# Generated by Django 4.0.10 on 2023-04-29 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=140)),
                ('telefone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=14)),
                ('endereco', models.CharField(max_length=200)),
                ('data_cadastro', models.DateField()),
            ],
        ),
    ]