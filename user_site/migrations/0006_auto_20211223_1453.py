# Generated by Django 3.2.6 on 2021-12-23 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0005_auto_20211211_1836'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Import',
            new_name='ImportExport',
        ),
        migrations.AlterModelOptions(
            name='importexport',
            options={'verbose_name': 'Import/Export', 'verbose_name_plural': 'Import/Export'},
        ),
    ]
