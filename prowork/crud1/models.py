from django.db import models


# Create your models here.

class dashboard(models.Model):
    acc_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()
 
    def __str__(self):
        return self.acc_name