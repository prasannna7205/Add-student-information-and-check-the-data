from django.db import models

# Create your models here.
class UserData(models.Model):
    name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    salary=models.IntegerField()
    address=models.CharField(max_length=100)