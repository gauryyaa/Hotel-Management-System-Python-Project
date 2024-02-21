from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField(max_length=10)
    aadhaar = models.IntegerField(max_length=12)
    room = models.CharField(max_length=10)
    days = models.IntegerField(max_length=2)

    def __str__(self):
        return self.name