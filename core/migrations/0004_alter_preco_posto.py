# Generated by Django 4.1.1 on 2022-09-23 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_preco_combustivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preco',
            name='posto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posto', to='core.posto'),
        ),
    ]
