from django.db import models

# Create your models here.



class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    iduser = models.IntegerField(default=0)
    user_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return "new notification, type: "+self.user_name + ", iduser : " + str(self.iduser)