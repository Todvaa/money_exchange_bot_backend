from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

STATUSES = (
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled')
    )
ROLES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('Developer', 'Developer'),
        ('Banned', 'Banned')
    )


class User(AbstractBaseUser):
    """Model for users"""
    id = models.BigIntegerField(
        primary_key=True,
        editable=False,
        unique=True,
        null=False
    )
    username = models.CharField(
        max_length=50,
        null=True
    )
    role = models.CharField(
        choices=ROLES,
        max_length=10,
        default='User'
    )
    referrer = models.ForeignKey(
        'self',
        null=True,
        on_delete=models.SET_NULL,
        default=None
    )
    fee = models.DecimalField(
        verbose_name='Fee',
        max_digits=7,
        decimal_places=2,
        default=0
    )
    paid_fee = models.DecimalField(
        verbose_name='Paid fee',
        max_digits=7,
        decimal_places=2,
        default=0
    )
    password = None
    last_login = None


class Request(models.Model):
    """Model for money exchange requests"""
    status = models.CharField(
        choices=STATUSES,
        max_length=10,
        default='Active'
    )
    creation_date = models.DateTimeField(
        verbose_name='Creation date',
        auto_now_add=True
    )
    city = models.CharField(
        verbose_name='Populated areas',
        max_length=20,
    )
    sold_currency = models.CharField(
        verbose_name='Sale currency',
        max_length=20,
    )
    sold_currency_amount = models.DecimalField(
        verbose_name='Amount of currency sold',
        max_digits=12,
        decimal_places=2
    )
    purchased_currency_amount = models.DecimalField(
        verbose_name='Amount of purchased currency',
        max_digits=12,
        decimal_places=0
    )
    currency_rate = models.DecimalField(
        verbose_name='Exchange rate',
        max_digits=7,
        decimal_places=2
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='owner_exchange_request'
    )
    commission_fee = models.DecimalField(
        verbose_name='Сommission',
        max_digits=7,
        decimal_places=2
    )

    class Meta:
        ordering = ['creation_date']
