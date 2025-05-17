from django.db import models

# Create your models here.


class Docs(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.TextField(max_length=100)
    phone = models.TextField(max_length=20)
    email = models.TextField(max_length=30)
    password = models.TextField(max_length=15)

    def __str__(self):
        return self.fullname + " " + self.email