from django.db import models

# Create your models here.
class Ruyxat(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tell = models.CharField(max_length=13, null=True)
    #bazaga qo'shilgan ma'lumot vaqtini saqlab boruvchi ustun o'zgarmas
    add_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
