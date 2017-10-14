from __future__ import unicode_literals
from django.db import models
import uuid
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class AppUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,phone_number ,gender):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            phone_number=phone_number,)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name,phone_number,gender):
        user = self.create_user(email, password=password,
         first_name=first_name, last_name=last_name,gender=gender,
         phone_number=phone_number)
        user.is_admin = True
        user.save(using=self._db)
        return user

class AppUser(AbstractBaseUser):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    GENDER_CHOICES = (
        (MALE,'MALE'),
        (FEMALE,'FEMALE'),
        (OTHERS,'OTHERS')
        )

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,blank=True)
    gender = models.CharField(max_length=1,default=MALE,choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = AppUserManager()
    USERNAME_FIELD = 'email'
    ALREADY_EXISTS = 'The user already exists'


class City(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=35)
    countrycode = models.ForeignKey('Country', db_column='CountryCode')
    district = models.CharField(db_column='District', max_length=20)
    population = models.IntegerField(db_column='Population')

    class Meta:
        db_table = 'city'


class Country(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, max_length=3)
    name = models.CharField(db_column='Name', max_length=52)
    continent = models.CharField(db_column='Continent', max_length=13)
    region = models.CharField(db_column='Region', max_length=26)
    surfacearea = models.FloatField(db_column='SurfaceArea')
    indepyear = models.SmallIntegerField(db_column='IndepYear', blank=True, null=True)
    population = models.IntegerField(db_column='Population')
    lifeexpectancy = models.FloatField(db_column='LifeExpectancy', blank=True, null=True)
    gnp = models.FloatField(db_column='GNP', blank=True, null=True)
    gnpold = models.FloatField(db_column='GNPOld', blank=True, null=True)
    localname = models.CharField(db_column='LocalName', max_length=45)
    governmentform = models.CharField(db_column='GovernmentForm', max_length=45)
    headofstate = models.CharField(db_column='HeadOfState', max_length=60, blank=True, null=True)
    capital = models.IntegerField(db_column='Capital', blank=True, null=True)
    code2 = models.CharField(db_column='Code2', max_length=2)

    class Meta:
        db_table = 'country'


class Countrylanguage(models.Model):
    countrycode = models.ForeignKey(Country, db_column='CountryCode')
    language = models.CharField(db_column='Language', max_length=30)
    isofficial = models.CharField(db_column='IsOfficial', max_length=1)
    percentage = models.FloatField(db_column='Percentage')

    class Meta:
        db_table = 'countrylanguage'
        unique_together = ('countrycode', 'language')

class UserSession(models.Model):
    user = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    otp = models.CharField(max_length=100)