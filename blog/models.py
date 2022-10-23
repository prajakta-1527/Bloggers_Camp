from django.db import models

# Create your models here.
class blogs(models.Model):
    sno=models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    content = models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    shortdesc=models.CharField(max_length=300, default="")
    def __str__(self):
        return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name +" "+ self.last_name