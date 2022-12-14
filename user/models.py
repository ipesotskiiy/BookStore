from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class UserModel(models.Model):
    email = models.EmailField(verbose_name='Your email', max_length=40, db_index=True)
    first_name = models.CharField(verbose_name='Your first name', max_length=30)
    last_name = models.CharField(verbose_name='Your last name', max_length=30, db_index=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class ProfileModel(models.Model):
    house = models.CharField(verbose_name='Your home', max_length=20)
    street = models.CharField(verbose_name='Your street', max_length=25)
    city = models.CharField(verbose_name='Your city', max_length=25, db_index=True)
    region = models.CharField(verbose_name='Your region', max_length=30, db_index=True)
    country = models.CharField(verbose_name='Your country', max_length=40, db_index=True)
    phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}',
                                 message="Phone number must be entered in the format: '+999999999'")
    phone_number = models.CharField('Phone', max_length=12, validators=[phone_regex], db_index=True)

