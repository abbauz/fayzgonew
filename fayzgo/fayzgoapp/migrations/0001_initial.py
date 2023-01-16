# Generated by Django 4.0.8 on 2023-01-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_uz', models.TextField(blank=True, max_length=1500, null=True)),
                ('about_ru', models.TextField(blank=True, max_length=1500, null=True)),
                ('about_en', models.TextField(blank=True, max_length=1500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=50, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=50, null=True)),
                ('name_en', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('description_uz', models.TextField(blank=True, max_length=1500, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=1500, null=True)),
                ('description_en', models.TextField(blank=True, max_length=1500, null=True)),
            ],
        ),
    ]