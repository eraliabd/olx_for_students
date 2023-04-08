import random
import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number must be set')

        user = self.model(
            phone_number=phone_number,
            # address=address,
            # gender=gender,
            # age=age,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(phone_number, password, **extra_fields)


MALE, FEMALE = (
    "male",
    "female"
)


class User(AbstractUser):
    _validate_phone = RegexValidator(
        regex=r'^998[0-9]{9}$',
        message="Telefon raqamingiz 9 bilan boshlanishi va 12 ta belgidan iborat bo'lishi kerak. Masalan: 998901235476"
    )
    GENDER_CHOICES = (
        (MALE, MALE),
        (FEMALE, FEMALE)
    )

    phone_number = models.CharField(max_length=20, unique=True, validators=[_validate_phone])
    address = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    age = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=100, default=f"user_{str(uuid.uuid4()).split('-')[-1]}")
    email = models.EmailField(unique=False, null=True, blank=True)
    USERNAME_FIELD = 'phone_number'

    objects = CustomUserManager()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


APARTMENT, COURTYARD = (
    'apartment', 'courtyard',
)
CONTRACT, NOCONTRACT = (
    'contract', 'nocontract'
)


class House(models.Model):
    HOUSE_TYPE = (
        (APARTMENT, APARTMENT),
        (COURTYARD, COURTYARD)
    )
    RENT_CONTRACT = (
        (CONTRACT, CONTRACT),
        (NOCONTRACT, NOCONTRACT)
    )
    rent_house = models.CharField(max_length=20, choices=HOUSE_TYPE)
    rent_contract = models.CharField(max_length=20, choices=RENT_CONTRACT)
    image = models.ImageField(upload_to='%Y/%m/%d')
    price = models.PositiveBigIntegerField()
    location = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
