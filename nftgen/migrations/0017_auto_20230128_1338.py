# Generated by Django 3.2.16 on 2023-01-28 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nftgen', '0016_delete_digital_art'),
    ]

    operations = [
        migrations.CreateModel(
            name='Digital_Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('init_image', models.ImageField(blank=True, default='default-noise.png', upload_to='initial_images/')),
                ('gen_image', models.ImageField(upload_to='generated_images/')),
                ('prompt', models.TextField()),
                ('iterations', models.IntegerField()),
                ('image_strength', models.DecimalField(decimal_places=1, max_digits=2)),
                ('run_time', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('seed', models.BigIntegerField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='digital_art', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Digital_Art',
                'verbose_name_plural': 'Digital_Art',
            },
        ),
        migrations.DeleteModel(
            name='Digital_Arts',
        ),
    ]
