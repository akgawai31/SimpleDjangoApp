from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name + "_" + self.last_name
    
