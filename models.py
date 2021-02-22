from django.db import models
from django import forms


class contact_details(models.Model):
    name = models.CharField(max_length=200)
    profile= models.ImageField(upload_to='images/',null=True, blank=True)
    mobile_no = models.IntegerField()
    address= models.TextField(max_length=400)
    email= models.CharField(max_length=500)


