# Generated by Django 3.2.6 on 2021-11-22 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0002_instance_image_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='routemodel',
            field=models.ImageField(blank=True, null=True, upload_to='routemodel/', verbose_name='Streckenmodell'),
        ),
    ]
