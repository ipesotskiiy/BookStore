# Generated by Django 4.1.4 on 2023-01-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0048_alter_book_price'),
        ('user', '0019_alter_user_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorites', to='product.book'),
        ),
    ]