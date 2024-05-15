# # from django.db import models

# # # accounts/models.py
# # from django.contrib.auth.models import User


# # class PDFFile(models.Model):
# #     name = models.CharField(max_length=255)
# #     file = models.FileField(upload_to='pdfs/')
# #     uploaded_at = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return self.name

# # # chat


# # class Message(models.Model):
# #     sender = models.ForeignKey(
# #         User, on_delete=models.CASCADE, related_name='sent_messages')
# #     receiver = models.ForeignKey(
# #         User, on_delete=models.CASCADE, related_name='received_messages')
# #     content = models.TextField()
# #     timestamp = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return f'{self.sender} -> {self.receiver}: {self.content}'

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db import models


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_doctor', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)


# class User(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=30)
#     age = models.IntegerField()
#     phone_number = models.CharField(max_length=10)
#     is_active = models.BooleanField(default=True)
#     is_doctor = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     objects = UserManager()

#     def __str__(self):
#         return self.email


# 1.........
"""
Module for defining models related to user authentication.
"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# 1
class UserManager(BaseUserManager):
    """
    Custom user manager for the User model.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create a new user.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create a new superuser.
        """
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    """
    Custom user model.
    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    # phone_number = models.CharField(max_length=10)
    # is_active = models.BooleanField(default=True)
    # is_doctor = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        """
        String representation of the user.
        """
        return str(self.email)


# 2
class PDFFile(models.Model):
    """
    Model representing a PDF file.
    """
    file = models.FileField(upload_to='pdfs/')
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


# 3
class Message(models.Model):
    """
    Represents a message stored in the database.
    This class defines a model for storing textual messages in the database.
    """
    message = models.TextField()

    def __str__(self):
        return str(self.message)
