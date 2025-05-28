from django.db import models

# Create your models here.


class Operation(models.Model):
    id = models.AutoField(primary_key=True)
    iduser = models.IntegerField(default=0)
    type_operation = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    detail = models.TextField(max_length=1000)

    def __str__(self):
        return "new operation, type: "+self.type_operation + ", iduser : " + str(self.iduser)