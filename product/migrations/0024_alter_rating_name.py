# Generated by Django 4.1.4 on 2022-12-27 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='name',
            field=models.PositiveIntegerField(max_length=3, verbose_name='Rating'),
        ),
    ]