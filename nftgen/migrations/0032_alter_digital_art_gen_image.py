# Generated by Django 3.2.16 on 2023-04-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nftgen', '0031_alter_digital_art_gen_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digital_art',
            name='gen_image',
            field=models.ImageField(blank=True, default='default-noise.png', null=True, upload_to='generated_images/'),
        ),
    ]
