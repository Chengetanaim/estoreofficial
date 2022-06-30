from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):

    # Add age field in create_user function if you had created it in the Account class

    def create_user(self, email, username, location, phone_number, profile_pic, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not location:
            raise ValueError('Users must have a location')
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not profile_pic:
            raise ValueError('Users must have a profile pic')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            location=location,
            phone_number=phone_number,
            profile_pic=profile_pic,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, location, phone_number, profile_pic):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            location=location,
            phone_number=phone_number,
            profile_pic=profile_pic,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)

    # The fields below are required for the Abstract Base User Class

    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=200)
    profile_pic = models.ImageField(models.ImageField(upload_to='images/'))


    # USERNAME_FIELD is a key word pointing to what field you want to login with (it can be username, email, etc)

    USERNAME_FIELD = 'email'

    # Fields you want for registration (could be username and first name and age etc)

    REQUIRED_FIELDS = ['username', 'location', 'phone_number', 'profile_pic']

    # Telling Django where the account manager is

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
