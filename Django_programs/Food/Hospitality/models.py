from django.contrib.auth import get_user_model
from django.db import models

User=get_user_model()
class Customer(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.TextField()
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()