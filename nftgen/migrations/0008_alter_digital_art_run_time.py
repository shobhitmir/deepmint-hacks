# Generated by Django 3.2.16 on 2023-01-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nftgen', '0007_alter_digital_art_init_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digital_art',
            name='run_time',
            field=models.IntegerField(default=20),
        ),
    ]
