# Generated by Django 3.2.6 on 2022-03-20 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nlp_component', '0010_auto_20220301_0220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='threshold',
            options={'verbose_name': 'Similarity threshold', 'verbose_name_plural': 'Similarity threshold'},
        ),
    ]