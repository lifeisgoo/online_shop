# Generated by Django 4.0.6 on 2022-09-15 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0005_productmodel_sale_alter_productmodel_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productmodel', verbose_name='product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'wishlist',
                'verbose_name_plural': 'wishlists',
                'unique_together': {('user', 'product')},
            },
        ),
    ]
