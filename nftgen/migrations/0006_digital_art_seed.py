# Generated by Django 3.2.16 on 2023-01-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nftgen', '0005_digital_art_prompt'),
    ]

    operations = [
        migrations.AddField(
            model_name='digital_art',
            name='seed',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
