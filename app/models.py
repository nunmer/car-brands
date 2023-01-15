from django.db import models

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=250)
    des = models.TextField()
    def __str__(self):
        return self.name