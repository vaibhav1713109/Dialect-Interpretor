from django.db import models

# Create your models here.
class ContactUs(models.Model):
    msg_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100,default='')
    phone=models.CharField(max_length=100,default='')
    desc=models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.username