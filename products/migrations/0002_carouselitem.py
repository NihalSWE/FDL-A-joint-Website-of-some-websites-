# Generated by Django 4.2.7 on 2024-07-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
    ]
