# Generated by Django 4.1.4 on 2022-12-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Your name'),
        ),
    ]
