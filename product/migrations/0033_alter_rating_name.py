# Generated by Django 4.1.4 on 2023-01-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0032_alter_rating_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='name',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Rating'),
        ),
    ]
