from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    social_id = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    mail_status = models.BooleanField()
    mail_status_discription = models.CharField(max_length=1000)

