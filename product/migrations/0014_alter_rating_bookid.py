# Generated by Django 4.1.4 on 2022-12-21 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='bookId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='product.book'),
        ),
    ]
