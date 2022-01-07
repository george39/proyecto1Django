# Generated by Django 4.0 on 2021-12-24 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Hbilidad',
                'verbose_name_plural': 'Hbilidades empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Departamento', 'verbose_name_plural': 'Area de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shor_name')},
        ),
    ]
