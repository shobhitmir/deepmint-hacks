# Generated by Django 3.2.16 on 2023-01-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nftgen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digital_art',
            name='gen_image',
            field=models.ImageField(upload_to='generated_images/'),
        ),
        migrations.AlterField(
            model_name='digital_art',
            name='init_image',
            field=models.ImageField(blank=True, default='initial_images/default-noise.png', upload_to='initial_images/'),
        ),
    ]
