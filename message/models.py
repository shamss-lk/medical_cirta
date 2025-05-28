from django.db import models

# Create your models here.


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    iduser = models.IntegerField(default=0)
    whoSend = models.CharField(max_length=20, default="user")
    content = models.TextField(max_length=1000)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "new message " + str(self.iduser) + str(self.content[0:10]) + "...."