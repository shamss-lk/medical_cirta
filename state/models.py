from django.db import models

# Create your models here.

class StateModel(models.Model):
    id = models.AutoField(primary_key=True)
    iduser = models.IntegerField(default=0)
    regime = models.TextField(max_length=100)
    coloscopie = models.CharField(max_length=100)
    sang = models.CharField(max_length=100)
    echo = models.CharField(max_length=100)
    poussee = models.CharField(max_length=100)
    symp = models.CharField(max_length=100)


    def __str__(self):
        return "new state " + str(self.iduser) + str(self.regime) + "...."