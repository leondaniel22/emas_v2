# Generated by Django 3.2.6 on 2022-03-20 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0009_auto_20220301_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Name'),
        ),
    ]