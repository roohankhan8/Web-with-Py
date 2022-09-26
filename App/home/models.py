from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    def __str__(self):
        return self.name
