from django.db import models
from django.utils import timezone
# Create your models here.
class ToDo(models.Model):
    title= models.CharField(max_length= 250)
    checked= models.BooleanField(default= False)
    created_at= models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.title