# # from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.core.validators import RegexValidator
# # from djongo import models
# from django.contrib.auth.models import Group, Permission
# from django.db import models


# # Create your models here.
# class CustomUser(AbstractUser):
#     email = models.EmailField(max_length=30) 
#     phone = models.BigIntegerField()
#     otp = models.CharField(max_length=6)
    

#     # Specify unique related_name attributes for groups and user_permissions
#     groups = models.ManyToManyField(Group, related_name='custom_user_groupss')
#     user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissionss')

# class Person(models.Model):
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     email = models.EmailField(max_length=30)
#     username = models.CharField(max_length=100,
#                                 validators=[RegexValidator (r'^[a-zA-Z0-9]*$',
#                                                             'Only alphanumeric characters are allowed.')])
#     password = models.CharField(max_length=200)

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)