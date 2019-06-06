from django.db import models


# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=10)
    retype=models.CharField(max_length=10)
    dob=models.DateField()
    def __str__(self):
        return self.name

class Blogs(models.Model):
    title=models.CharField(max_length=50)
    blog=models.CharField(max_length=300)
    pic=models.FileField(upload_to='images/')
    upload_date=models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=30)
    def __str__(self):
        return self.title
