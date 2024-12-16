"""
Module for defining models related to user authentication.
"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


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
        extra_fields.setdefault('is_active', True)  # Default to active users
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create a new superuser.
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    """
    Custom user model.
    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        """
        String representation of the user.
        """
        return str(self.email)


class PDFFile(models.Model):
    """
    Model representing a PDF file.
    """
    file = models.FileField(upload_to='pdfs/')
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()  # Define objects manager explicitly

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    """
    Represents a message stored in the database.
    This class defines a model for storing textual messages in the database.
    """
    message = models.TextField()
    objects = models.Manager()  # Define objects manager explicitly

    def __str__(self):
        return str(self.message)
