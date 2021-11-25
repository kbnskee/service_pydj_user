from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string
from django.core.mail import send_mail


class CustomBaseUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None):
        if not username:
            raise ValueError("Username is required")
        if not password:
            raise ValueError("Password is required")

        user = self.model(
            username = self.username,
            email = self.normalize_email(email)            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def admin_create_user(self, username=None, email=None):
        if not email:
            raise ValueError("Email is required")

        init_password = get_random_string(length=18)
        user = self.create_user(username, email, password=init_password)
        send_mail(
            'User Registration',
            'Please log in using the following creds ' + init_password,
            'karlkevinddomingo@gmamil.com',
            ['karlkdomingo@gmail.com'],
            fail_silently=False,
        )
        return user
    

class CustomAbstractBaseUser(AbstractBaseUser):    
    class Meta:
        db_table = '"users"'

    username = models.CharField(max_length=225, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=225, unique=True, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username', 'password'] 

    object = CustomBaseUserManager()

    def __str__(self):
        return self.username

    @property
    def is_ctive(self):
        return self.active