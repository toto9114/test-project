from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    SEX_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.CharField(max_length=100)
    nickname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    sex = models.IntegerField(choices=SEX_CHOICE, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class Order(models.Model):
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders', related_query_name='order')
    order_number = models.CharField(max_length=12)
    product_name = models.CharField(max_length=100)
    dt_order = models.DateTimeField(auto_now_add=True)
