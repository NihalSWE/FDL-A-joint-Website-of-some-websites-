# Generated by Django 4.2.7 on 2024-07-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_contactformdata_contactstaticcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactstaticcontent',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contactstaticcontent',
            name='map_embed_url',
            field=models.TextField(),
        ),
    ]
