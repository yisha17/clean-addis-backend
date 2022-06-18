from re import T
from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.forms import CharField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import AbstractUser
from requests import delete
# Create your models here.


class Address(models.Model):

    class meta:
        verbose_name_plural = 'Addresses'
    
    SUBCITY_CHOICES = [
        ('Addis Ketema','AK'),
        ('Bole','Bole'),
        ('Nifas Silk','NS'),
        ('Kolfe','Kolfe')

    ]

    subcity = models.CharField(max_length=20,choices=SUBCITY_CHOICES,default='B')
    woreda = models.IntegerField(default=1)


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class User(AbstractUser):

    ROLE = [
        ('Qorale','Qorale'),
        ('Garbage Collector', 'Garbage Collector'),
        ('City Admin','City Admin'),
        ('Resident','Resident')
    ]

    username = models.CharField(max_length=20,unique=True, default="")
    email = models.EmailField(max_length=30,default="")
    role = models.CharField(max_length=20,choices=ROLE, default="Resident", null = True)
    profile = models.ImageField(upload_to= upload_to, null=True)
    phone = models.CharField(max_length= 20,null= True)
    address = models.CharField(max_length=40,null = True)
    
    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'




class Company(models.Model):

    class meta:
        verbose_name_plural = 'Companies'
    company_name = models.CharField(max_length=20)
    company_email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    logo = models.ImageField(null = True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


    def __str__(self):
        return self.company_name



class Waste(models.Model):

    

    TYPE_CHOICES = [
        ('Plastic', 'Plastic'),
        ('Organic','Organic'),
        ('Metal','Metal'),
        ('Aluminium', 'Almuinium'),
        ('Paper','Paper'),
        ('E-waste','E-waste'),
        ('Glass','Glass'),
        ('Fabric','Fabric')
    ]

    DO = [
        ('Sell', 'Sell'),
        ('Donation', 'Donation'),
    ]

    seller = models.ForeignKey(
        User, on_delete=models.CASCADE)
    buyer = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name='buyer', db_constraint=False)
    waste_name = models.CharField(max_length=20)
    waste_type = models.CharField(max_length=20, choices= TYPE_CHOICES)
    for_waste  = models.CharField(choices= DO, max_length =10)
    price_per_unit = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    metric = models.CharField(null=True, max_length = 20)
    image = models.ImageField(upload_to = upload_to, null = True)
    location = models.CharField(max_length=30,null=True)
    sold = models.BooleanField(null=True)
    bought = models.BooleanField(null=True)
    donated = models.BooleanField(null=True)
    description = models.CharField(max_length=200,null=True)
    post_date = models.DateTimeField(auto_now_add=True)

class Report(models.Model):

    
    reportTitle = models.CharField(max_length=120,default="",null=True)
    reportDescription = models.CharField(max_length=320,default="",null=True)
    isResolved = models.BooleanField(default= False)
    image = models.ImageField(upload_to=upload_to, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=10)
    latitude = models.DecimalField(max_digits=12, decimal_places=10)
    reportedBy = models.ForeignKey(User, on_delete = models.DO_NOTHING,null= True )
    post_date = models.DateTimeField(auto_now_add=True)
    
class PublicPlace(models.Model):

    TYPE_CHOICES = [
        ('Toilet', 'Toilet'),
        ('Park','Park')
    ]
    placeName = models.CharField(max_length=120,default="",null=True)
    placeType = models.CharField(max_length=120, choices= TYPE_CHOICES)
    rating = models.IntegerField( null=True)
    longitude = models.DecimalField(max_digits= 14,decimal_places=10,unique=True )
    latitude = models.DecimalField(max_digits=14, decimal_places=10, unique=True)

    


class Seminar(models.Model):
    TYPE_CHOICES = [
        ('Meeting','Meeting'),
        ('Plantation','Plantation'),
        ('Cleaning','Cleaning')
    ]

    seminarTitle = models.CharField(max_length=120,default="",null=True)
    seminarType = models.CharField(max_length=20, choices= TYPE_CHOICES)
    link = models.CharField(max_length=200,default = "")
    imageLink = models.CharField(max_length = 300, default="")
    fromDate = models.DateTimeField(auto_now_add=True)
    toDate = models.DateField( null=True)
    isExpired = models.BooleanField(default=False)

class WorkSchedule(models.Model):
    date = models.DateField(null=True)
    hour = models.DateField(null=True)
    
class Announcement(models.Model):
    TYPE_CHOICES = [
        ('Report','Report'),
        ('Announcement','Announcement'),
        ('Waste','Waste')
    ]
    notification_title = models.CharField(max_length=20, default="",null=True)
    notification_body = models.CharField(max_length=120, default="",null=True)
    notification_type = models.CharField(max_length=30)
    published = models.DateField(null=True)
    owner = models.ForeignKey(User,on_delete=DO_NOTHING,null=True,related_name='owner')
    point_to_report = models.ForeignKey(Report,on_delete=DO_NOTHING,null=True)
    point_to_waste = models.ForeignKey(Waste,on_delete=DO_NOTHING,null=True)
    address = models.CharField(max_length=40,null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
    buyer = models.ForeignKey(User,on_delete=DO_NOTHING,null=True,related_name='can_buy')

class Notifications(models.Model):
    isSeen = models.BooleanField(default=False)
    notificationtype = models.CharField(max_length=10,)
    user = models.IntegerField()
    point_to = models.IntegerField()
    post_date = models.DateTimeField(auto_now_add=True)
    



