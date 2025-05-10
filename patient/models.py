from django.db import models

# Create your models here.


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.TextField(max_length=100)
    address = models.TextField(max_length=200)
    phone = models.TextField(max_length=20)
    email = models.TextField(max_length=30)
    password = models.TextField(max_length=15)
    disease = models.TextField(max_length=500, default='')
    detail = models.TextField(max_length=3000 , default='')

    def __str__(self):
        return self.fullname + " " + self.email