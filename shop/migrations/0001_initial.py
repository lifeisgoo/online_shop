# Generated by Django 4.0.6 on 2022-07-26 16:46

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ProductTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('short_description', models.CharField(max_length=255, verbose_name='short_description')),
                ('long_description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='long_description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='price')),
                ('sale', models.PositiveSmallIntegerField(default=0, verbose_name='sale')),
                ('main_image', models.ImageField(upload_to='products/', verbose_name='main_image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='shop.categorymodel', verbose_name='category')),
                ('tag', models.ManyToManyField(related_name='products', to='shop.producttagmodel', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
