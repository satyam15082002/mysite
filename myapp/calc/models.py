from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def say(self):
        return f"{self.name},{self.password}"