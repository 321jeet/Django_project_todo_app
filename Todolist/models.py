from operator import mod
from django.db import models

# Create your models here.
class TODO(models.Model):
    text=models.CharField(max_length=200 ,default='')
    time=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.text