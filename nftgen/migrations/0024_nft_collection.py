# Generated by Django 3.2.16 on 2023-03-14 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nftgen', '0023_delete_nft_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='NFT_Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_address', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'NFT_Collection',
                'verbose_name_plural': 'NFT_Collection',
            },
        ),
    ]