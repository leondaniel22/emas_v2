# Generated by Django 3.2.6 on 2022-02-21 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0007_alter_solution_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solution',
            options={'verbose_name': 'Lösungsmaßnahme', 'verbose_name_plural': 'Lösungsmaßnahmen'},
        ),
    ]
